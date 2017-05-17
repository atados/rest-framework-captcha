from django.test import TestCase
from rest_framework_captcha.models import Captcha as CaptchaModel
from rest_framework_captcha.captcha import Captcha

class CaptchaViewTestCase(TestCase):
  def test_captcha_route_returns_captcha_id_header(self):
    pass

  def test_creating_route_returns_correct_content_type(self):
    pass
