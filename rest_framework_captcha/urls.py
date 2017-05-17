from rest_framework_captcha import views
from django.conf.urls import url

urlpatterns = [
  url(r'^captcha/', views.generate_captcha, name='generate-captcha'),
]
