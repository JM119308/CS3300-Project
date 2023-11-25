from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles =[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			print('role', allowed_roles)
			gorup = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name 
			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
				
			else:
					return HttpResponse('You do not have permission to access this page')
		return wrapper_func
	return decorator