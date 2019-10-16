import json
from tornado import gen, web
from jupyter_server.base.handlers import path_regex
from jupyter_server.services.contents.handlers import ContentsHandler as BaseContentsHandler

from jupyterhub.services.auth import HubAuthenticated

from .auth import authorized



error = web.HTTPError(status_code=401, log_message="Unauthorized. User doesn't have access to resource")

class ContentsHandler(HubAuthenticated, BaseContentsHandler):

    @property
    def enforcer(self):
        return self.settings['enforcer']

    def user_is_authorized(self, user, action):
        # Is the user authorized to do this action?
        name = user['name']
        if self.enforcer.enforce(name, action):
            return True
        return False

    @web.authenticated
    @authorized('read', error=error)
    @gen.coroutine
    def get(self, path=''):
        """Return a model for a file or directory.

        A directory model contains a list of models (without content)
        of the files and directories it contains.
        """
        super(ContentsHandler, self).get(path=path)

    @web.authenticated
    @authorized('rename', error=error)
    @gen.coroutine
    def patch(self, path=''):
        """PATCH renames a file or directory without re-uploading content."""
        super(ContentsHandler, self).patch(path=path)

    @authorized('copy', error=error)
    @gen.coroutine
    def _copy(self, copy_from, copy_to=None):
        """Copy a file, optionally specifying a target directory."""
        super(ContentsHandler, self)._copy(copy_from, copy_to=copy_to)

    @authorized('upload', error=error)
    @gen.coroutine
    def _upload(self, model, path):
        """Handle upload of a new file to path"""
        super(ContentsHandler, self)._upload(model, path)

    @authorized('new', error=error)
    @gen.coroutine
    def _new_untitled(self, path, type='', ext=''):
        """Create a new, empty untitled entity"""
        super(ContentsHandler, self)._new_untitled(path, type=type, ext=ext)

    @authorized('save', error=error)
    @gen.coroutine
    def _save(self, model, path):
        """Save an existing file."""
        super(ContentsHandler, self)._save(model, path)

    @web.authenticated
    @gen.coroutine
    def post(self, path=''):
        """Create a new file in the specified path.

        POST creates new files. The server always decides on the name.

        POST /api/contents/path
          New untitled, empty file or directory.
        POST /api/contents/path
          with body {"copy_from" : "/path/to/OtherNotebook.ipynb"}
          New copy of OtherNotebook in path
        """
        super(ContentsHandler, self).post(path=path)

    @web.authenticated
    @gen.coroutine
    def put(self, path=''):
        """Saves the file in the location specified by name and path.

        PUT is very similar to POST, but the requester specifies the name,
        whereas with POST, the server picks the name.

        PUT /api/contents/path/Name.ipynb
          Save notebook at ``path/Name.ipynb``. Notebook structure is specified
          in `content` key of JSON request body. If content is not specified,
          create a new empty notebook.
        """
        super(ContentsHandler, self).put(path=path)

    @web.authenticated
    @authorized('delete', error=error)
    @gen.coroutine
    def delete(self, path=''):
        """delete a file in the given path"""
        super(ContentsHandler, self).delete(path=path)

default_handlers = [
    (r"/jhubshare%s" % path_regex, ContentsHandler),
]


