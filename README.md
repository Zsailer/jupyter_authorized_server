# Jupyter Server with Authorization

An experimental project adding authorization to Jupyter's core services.

Adds an `authorized` wrapper (i.e. decorator) to Jupyter Server's tornado handlers to check which actions are allowed for the `current_user`.

Clone this repo;
```
git clone https://github.com/Zsailer/jupyter_authorized_server
```
Install the dev version using pip:
```
pip install -e .
```
