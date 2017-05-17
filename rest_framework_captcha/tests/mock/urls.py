from django.conf.urls import url

from rest_framework_captcha.urls import urlpatterns
from rest_framework_captcha.tests.mock import views

urlpatterns += [
  url(r'^protect-view/', views.protected_view, name='protected-view'),
]
