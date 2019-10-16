


def authorized(action, error=None):
    if not error:
        error = Exception('401: Unauthorized.')

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
