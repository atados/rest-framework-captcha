from django.test import TestCase
from rest_framework_captcha.models import Captcha as CaptchaModel
from rest_framework_captcha.captcha import Captcha

class CaptchaTestCase(TestCase):
  def test_creating_captcha_object_creates_model(self):
    self.assertTrue(CaptchaModel.objects.count() == 0)
    captcha = Captcha()
    self.assertTrue(CaptchaModel.objects.count() == 1)

  def test_creating_captcha_object_generates_image(self):
    captcha = Captcha()
    self.assertTrue(captcha.image)
