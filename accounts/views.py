from django.shortcuts import render,redirect
from .utils import generate_otp, send_otp_via_sms
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login,logout
from django.http import HttpResponse
from datetime import timedelta
from .models import CustomUser
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.decorators import login_required

OTP_VALID_MINUTES = 10

def request_otp_view(request):
    if request.method == 'POST':
        phone = request.POST.get("phone_number","").strip()
        if not phone:
            messages.error(request,"Enter phone_number.")
            return redirect("request_otp")
        user,created = CustomUser.objects.get_or_create(phone_number=phone)
        otp = generate_otp()
        user.otp_code = otp
        user.otp_created_at = timezone.now()
        user.otp_used = False
        user.save(update_fields=['otp_code','otp_created_at','otp_used'])
        send_otp_via_sms(phone,otp)
        print('request otp ran')
        request.session['otp_phone'] = phone
        return redirect('verify_otp')
    return render(request,"enter_phone.html")


def verify_otp_view(request):
    phone = request.session.get("otp_phone")
    if request.method == "POST":
        phone = request.POST.get("phone_number",phone)
        otp_entered = request.POST.get("otp","").strip()

        if not phone or not otp_entered:
            messages.error(request,"Phone and OTP required.")
            return redirect("request_otp")
        try:
            user = CustomUser.objects.get(phone_number=phone)
        except CustomUser.DoesNotExist:
            messages.error(request,"Invalid phone number. Request OTP first.")
            return redirect('request_otp')
        if user.otp_used:
            messages.error(request,"This otp has already been used.Request a new one.")
            return redirect("request.otp")

        if not user.otp_created_at or timezone.now()-user.otp_created_at > timedelta(minutes=OTP_VALID_MINUTES):
            messages.error(request,'OTP expired.Request a new OTP.')
            return redirect("request_otp")
        if otp_entered != user.otp_code:
            messages.error(request,"Invalid OTP")
            return redirect("verify_otp")
        user.otp_used = True
        user.otp_code = None
        user.otp_created_at = None
        user.save(update_fields=['otp_used','otp_code','otp_created_at'])
        user.backend='django.contrib.auth.backends.ModelBackend'
        login(request,user)
        request.session.pop('otp_phone',None)
        return redirect('store')
    return render(request,'enter_otp.html')

def logout_view(request):
    logout(request)
    return redirect('store')

@login_required(login_url='/accounts/request-otp/')
def profile(request):
    return render(request,'profile.html')
def custom_404(request,exception):
    return render(request,'404.html',status=404)

# Create your views here.
