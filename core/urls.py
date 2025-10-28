from django.urls import path
from django.conf.urls import handler404
from . import views

handler404 = 'core.views.custom_404'
urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
]