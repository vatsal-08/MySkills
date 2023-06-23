from django.shortcuts import redirect
from django.contrib import messages

class AdminSuperuserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and not request.user.is_superuser:
            messages.error(request, 'You are not authorized to access the admin panel.')
            return redirect('courses')
        
        response = self.get_response(request)
        return response
