from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect




def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.is_authenticated:
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in ['employee']:
              return HttpResponseForbidden("You don't have permission to access this page.")
            
            elif group in ['admin']:
                return view_func(request, *args, **kwargs)

            else:
                return HttpResponseForbidden("You don't have permission to access this page.")
        else:
            return redirect('home')
    return wrapper_func