
from django.contrib import admin
from django.urls import path
from phone_market.views import home, basket, contact, register, telephones, tel_detail, add_basket

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="bosh_sahifa" ),
    path('telephone/', telephones, name="telephone" ),
    path('contact/', contact, name="contact" ),
    path('basket/', basket, name="basket" ),
    path('register/', register, name="register" ),
    path('telephone/<int:tel_id>', tel_detail, name="tel_detail"),
    path('add_basket/<int:tel_id>', add_basket, name="add_basket")
  
]
