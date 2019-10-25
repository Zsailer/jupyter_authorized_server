import os
from jupyter_server.transutils import _
from jupyter_server.serverapp import ServerApp, load_handlers

from jupyterhub.services.auth import HubAuth

from traitlets import Unicode, default

import casbin

class AuthorizedServerApp(HubAuth, ServerApp):

    name = 'jhubshare'
    description = _("""The Jupyter Server with authorization""")
    port = 9999

    # Let's not serve any of jupyter's core services
    default_services = []

    # But let's add the new (patched) contents service.
    extra_services = [
        'jupyter_authorized_server.contents'
    ]

    # Files to pull authorization details from.
    model_file = Unicode('model.conf', config=True)
    policy_file = Unicode('policy.csv', config=True)

    # Setup URLs.
    default_url = "/services/jhubshare"
    base_url = Unicode(config=True)

    @default('base_url')
    def _default_base_url(self):
        try:
            base_url = os.environ['JUPYTERHUB_SERVICE_PREFIX']
        except KeyError:
            raise Exception("no url found.")
        return base_url        

    api_token = Unicode(config=True)

    @default('api_token')
    def _default_api_token(self):
        try:
            api_token = os.environ['JUPYTERHUB_API_TOKEN']
        except KeyError:
            raise Exception(
                "No API token was found in the environment variables. "
                "Are you running this as a hub-managed service?"
            )
        return api_token


    def initialize_enforcer(self):
        self.enforcer = casbin.Enforcer(self.model_file, self.policy_file)
        self.tornado_settings['enforcer'] = self.enforcer

    def initialize(self, argv=None, load_extensions=False):
        super(ServerApp, self).initialize(argv)
        self.init_logging()
        self.init_configurables()
        self.init_components()
        self.initialize_enforcer()
        self.init_webapp()
        self.init_signal()
        self.init_mime_overrides()
        self.init_shutdown_no_activity()


main = AuthorizedServerApp.launch_instance