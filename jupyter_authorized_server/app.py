from jupyter_server.transutils import _
from jupyter_server.serverapp import ServerApp, load_handlers

from jupyterhub.services.auth import HubAuth

from traitlets import Unicode


class AuthorizedServerApp(HubAuth, ServerApp):
    name = 'jhubshare'
    description = _("""The Jupyter Server with authorization""")
    port = 9999
    default_url = "/jhubshare"
    api_token=Unicode(config=True)
    base_url = '/services'
    default_services = []
    extra_services = [
        'jupyter_authorized_server.contents'
    ]


main = AuthorizedServerApp.launch_instance