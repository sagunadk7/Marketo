from django.contrib import admin
from django.urls import path,include
from service.views import store



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',store,name='store'),
    path('accounts/',include('core.urls')),
    path('services/',include('service.urls'))
]
