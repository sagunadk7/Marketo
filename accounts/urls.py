from django.urls import path
from django.conf.urls import handler404
from . import views

handler404 = 'core.views.custom_404'
urlpatterns = [
    path("request-otp/", views.request_otp_view, name="request_otp"),
    path("verify-otp/", views.verify_otp_view, name="verify_otp"),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile,name='profile'),
]