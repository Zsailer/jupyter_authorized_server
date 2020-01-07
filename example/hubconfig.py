# from jupyterhub.auth import DummyAuthenticator
# from jupyterhub.spawner import SimpleLocalProcessSpawner

# c.JupyterHub.services = [
#     {
#         'name': 'jhubshare',
#         'admin': False,
#         'url': 'http://127.0.0.1:9999',
#         'command': ['jupyter', 'authorized-server']
#     }
# ]

# c.JupyterHub.authenticator_class = DummyAuthenticator
# c.JupyterHub.spawner_class = SimpleLocalProcessSpawner
# c.JupyterHub.home_dir = '{username}'