from jupyter_server.transutils import _
from jupyter_server.serverapp import ServerApp, load_handlers


class AuthorizedServerApp(ServerApp):
    name = 'jupyter-authorized-server'
    description = _("""The Jupyter Server with authorization""")

    default_services = []
    extra_services = [
        'jupyter_authorized_server.contents'
    ]


main = AuthorizedServerApp.launch_instance