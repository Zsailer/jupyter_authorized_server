# Jupyter Server with Authorization

An experimental project adding authorization to Jupyter's core services. This allows multiple users to access the **same** Jupyter Server.

Adds an `authorized` wrapper (i.e. decorator) to Jupyter Server's tornado handlers to check which actions are allowed for the `current_user`.

Currently, this project only provides Jupyter's Contents API—it acts like a shared drive. We can expand this to other Jupyter services, i.e. kernels.

## Try it out!

`jupyter_authorized_server` can be run as a [JupyterHub Service](https://jupyterhub.readthedocs.io/en/stable/reference/services.html#services). This enables JupyterHub to be the provider of authenticated users. Authorization is (currently) pulled from a policy.csv file. In the future, we can source this information from the authenticators in JupyterHub.

Run the following example from the `/example` folder and follow these steps. 

1. Install JupyterHub and the jupyter_authorized_server:
    ```
    pip install jupyterhub
    git clone https://github.com/Zsailer/jupyter_authorized_server
    cd jupyter_authorized_server
    pip install -e .
    ```
2. Navigate to the `/example` folder
3. Run `sh hub.sh`.
4. Open your browser window, and go to the hub's homepage: http://localhost:8000
5. Sign in as `alice`. 
6. Visit http://localhost:8000/services/jhubshare/contents/hubconfig.py
    You should see the server response with a JSON blog that contains the contents of the `hubconfig.py` file.
7. Return to the hub's homepage: http://localhost:8000/
8. Sign out of `alice`'s account and sign-in as `bob`.
9. Visit http://localhost:8000/services/jhubshare/contents/hubconfig.py
    You should see an `Unauthorized` error.