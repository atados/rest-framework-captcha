from django.http import HttpResponse

from rest_framework_captcha.captcha import Captcha

def generate_captcha(request):
  captcha = Captcha()

  return HttpResponse(captcha.image, content_type="image/png")
