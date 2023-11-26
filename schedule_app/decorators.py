from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name__in=allowed_roles).exists():
                return view_func(request, *args, **kwargs)
            else:
                # Redirect to login or a forbidden page
                return redirect('login')  # Adjust the URL as needed
        return wrapper
    return decorator