from jupyter_server.transutils import _
from jupyter_server.serverapp import ServerApp, load_handlers

from jupyterhub.services.auth import HubAuth

from traitlets import Unicode

import casbin

class AuthorizedServerApp(HubAuth, ServerApp):

    name = 'jhubshare'
    description = _("""The Jupyter Server with authorization""")
    port = 9999
    default_url = "/jhubshare"
    api_token=Unicode('model.conf', config=True)
    base_url = '/services'
    default_services = []
    extra_services = [
        'jupyter_authorized_server.contents'
    ]
    model_file = Unicode('model.conf', config=True)
    policy_file = Unicode('policy.csv', config=True)

    def initialize_enforcer(self):
        self.enforcer = casbin.Enforcer(self.model_file, self.policy_file)
        self.tornado_settings['enforcer'] = self.enforcer

    def initialize(self, argv=None, load_extensions=False):
        super(ServerApp, self).initialize(argv)
        self.init_logging()
        if self._dispatching:
            return
        self.init_configurables()
        if load_extensions:
            self.init_server_extension_config()
        self.init_components()
        self.initialize_enforcer()
        self.init_webapp()
        self.init_terminals()
        self.init_signal()
        if load_extensions:
            self.init_server_extensions()
        self.init_mime_overrides()
        self.init_shutdown_no_activity()


main = AuthorizedServerApp.launch_instance