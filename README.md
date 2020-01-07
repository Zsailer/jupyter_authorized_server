# Jupyter Server with Authorization

An experimental project adding authorization to Jupyter's core services. This allows multiple users to access the **same** Jupyter Server.

Adds an `authorized` wrapper (i.e. decorator) to Jupyter Server's tornado handlers to check which actions are allowed for the `current_user`.

The server's authorization layer is highly configurable. I don't make many decisions for you—keeping it as general as possible.

## How?

Each handler in the Jupyter Server checks whether the current user is authorized the make the current request. This is determined by an `user_is_authorized` method in each handler. By default, this evaluates to `True`. You can patch this method in Jupyter Server's base handler, `JupyterHandler`, to implement your own authorization method.

There are three types of permissions: "read", "write" and "execute".

* "read" refers to all `GET` and `HEAD` requests.
* "write" refers to all `PUT`, `PATCH`, `POST`, and `DELETE` requests.
* "execute" refers to all requests to ZMQ/Websocket channels.