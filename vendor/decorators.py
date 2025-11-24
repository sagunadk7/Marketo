from django.shortcuts import redirect
from django.utils.http import urlencode
def vendor_required(view_func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated or not request.user.is_vendor():
            request.session['next_url'] = request.path
            return redirect('request_otp')
        return view_func(request,*args,**kwargs)
    return wrapper

def customer_required(view_func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated or not request.user.is_customer():
            request.session['next_url'] = request.path
            return redirect('request_otp')
        return view_func(request,*args,**kwargs)
    return wrapper
