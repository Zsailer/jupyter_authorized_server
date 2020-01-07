# Jupyter Server with Authorization

An experimental project adding authorization to Jupyter's core services. This allows multiple users to access the **same** Jupyter Server.

Adds an `authorized` wrapper (i.e. decorator) to Jupyter Server's tornado handlers to check which actions are allowed for the `current_user`.

The server's authorization layer is highly configurable. I don't make many decisions for you—keeping it as general as possible.

## How?

Each handler in the Jupyter Server checks whether the current user is authorized the make the current request. This is determined by an `user_is_authorized` method in each RequestHandler. By default, this evaluates to `True`. You can patch this method in Jupyter Server's base handler, `JupyterHandler`, to implement your own authorization method.

There are three types of permissions: "read", "write" and "execute".

* "read" refers to all `GET` and `HEAD` requests.
* "write" refers to all `PUT`, `PATCH`, `POST`, and `DELETE` requests.
* "execute" refers to all requests to ZMQ/Websocket channels.

Each of Jupyter Server's services are encoded to require one of the above permissions. Users without permission see a `401` error.

Each service is also encoded with a "resource-type" label, e.g. "contents", "kernels", "channels", etc. This enables finer grained access management. For example, this layer can be configured to allow users to change directories, read and execute notebooks, but not save any changes they make—behaving much like a temporary notebook server (see the [examples](/examples) folder).

## Install

Clone from source, change into the base directory, and install using `pip`:
```
pip install -e .
```

# Basic Example

Once you've installed the authorized server, try out the example in the `example/` directory. You'll need [NBClassic](https://github.com/Zsailer/nbclassic), a classic Jupyter Notebook frontend for Jupyter Server, to get test it out. Read the README there for more details.