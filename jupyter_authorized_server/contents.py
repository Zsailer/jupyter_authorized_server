import json
from tornado import gen, web
from jupyter_server.base.handlers import path_regex
from jupyter_server.services.contents.handlers import ContentsHandler as BaseContentsHandler

from jupyterhub.services.auth import HubAuthenticated

from .auth import authorized

class ContentsHandler(HubAuthenticated, BaseContentsHandler):

    # def get_current_user(self):
    #     return 'zsailer'

    def user_is_authorized(self, user, action):
        print(f"\n\n\n\n{user} {action}\n\n\n")
        return True

    @web.authenticated
    @authorized('read')
    @gen.coroutine
    def get(self, path=''):
        """Return a model for a file or directory.

        A directory model contains a list of models (without content)
        of the files and directories it contains.
        """
        super(ContentsHandler, self).get(path=path)

    @web.authenticated
    @authorized('rename')
    @gen.coroutine
    def patch(self, path=''):
        """PATCH renames a file or directory without re-uploading content."""
        super(ContentsHandler, self).patch(path=path)

    @authorized('copy')
    @gen.coroutine
    def _copy(self, copy_from, copy_to=None):
        """Copy a file, optionally specifying a target directory."""
        super(ContentsHandler, self)._copy(copy_from, copy_to=copy_to)

    @authorized('upload')
    @gen.coroutine
    def _upload(self, model, path):
        """Handle upload of a new file to path"""
        super(ContentsHandler, self)._upload(model, path)

    @authorized('new')
    @gen.coroutine
    def _new_untitled(self, path, type='', ext=''):
        """Create a new, empty untitled entity"""
        super(ContentsHandler, self)._new_untitled(path, type=type, ext=ext)

    @authorized('save')
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
    @authorized('delete')
    @gen.coroutine
    def delete(self, path=''):
        """delete a file in the given path"""
        super(ContentsHandler, self).delete(path=path)

default_handlers = [
    (r"/jhubshare%s" % path_regex, ContentsHandler),
]


