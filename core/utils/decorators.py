from functools import wraps
from django.contrib.auth.decorators import login_required

def method_login_required(view_func):
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        return login_required(login_url='core:login')(
            lambda req, *a, **kw: view_func(self, req, *a, **kw)
        )(request, *args, **kwargs)
    return wrapper 