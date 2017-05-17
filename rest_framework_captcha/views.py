from django.http import HttpResponse

from rest_framework_captcha.captcha import Captcha

def generate_captcha(request):
  captcha = Captcha()
  response = HttpResponse(captcha.image, content_type="image/png")
  response["X-Captcha-UUID"] = captcha.model_instance.uuid

  return response
