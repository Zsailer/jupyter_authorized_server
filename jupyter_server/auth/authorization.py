"""Provides a decorator used by Tornado RequestHandlers to
verify that a user is authorized to perform an action
"""
import functools
from tornado.web import HTTPError


def authorized(action):
    """A decorator for tornado.web.RequestHandler methods
    that verifies whether the current user is authorized
    to use the following method.

    Helpful for adding an 'authorization' layer to
    a REST API.
    """
    error = HTTPError(
        status_code=401,
        log_message="Unauthorized. User is not allowed to XX."
    )

    def wrapper(method):

        def inner(self, *args, **kwargs):
            user = self.current_user
            # If the user is allowed to do this action,
            # call the method.
            if self.user_is_authorized(user, action):
                return method(self, *args, **kwargs)
            # else raise an exception.
            else:
                raise error
        return inner

    return wrapper
