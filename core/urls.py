
from django.contrib import admin
from django.urls import path
from phone_market.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="bosh_sahifa" )
]
