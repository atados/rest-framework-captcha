from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from django.utils import timezone
from dateutil import relativedelta

from rest_framework.test import APIClient
from rest_framework_captcha.models import Captcha as Captcha

class CaptchaViewTestCase(TestCase):
  def setUp(self):
    self.client = Client()

  def test_captcha_route_returns_captcha_id_header(self):
    response = self.client.get(reverse("generate-captcha"))
    self.assertTrue(len(response["X-Captcha-UUID"]))

  def test_creating_route_returns_correct_content_type(self):
    response = self.client.get(reverse("generate-captcha"))
    self.assertTrue(response["Content-Type"] == "image/png")


class ProtectedViewTestCase(TestCase):
  def setUp(self):
    self.client = APIClient()

  def test_view_is_protected(self):
    response = self.client.get(reverse("protected-view"))
    self.assertTrue(response.status_code == 400)

  def test_can_access_view_with_correct_header(self):
    captcha = Captcha(secret="abc")
    captcha.save()

    response = self.client.get(reverse("protected-view"), HTTP_X_CAPTCHA_UUID=captcha.uuid, HTTP_X_CAPTCHA_SECRET="abc")
    self.assertTrue(response.status_code == 200)

    return captcha

  def test_cant_reuse_captcha(self):
    captcha = self.test_can_access_view_with_correct_header()

    response = self.client.get(reverse("protected-view"), HTTP_X_CAPTCHA_UUID=captcha.uuid, HTTP_X_CAPTCHA_SECRET="abc")
    self.assertTrue(response.status_code == 400)

  def test_cant_captcha_expiry_time(self):
    captcha = Captcha(secret="abc")
    captcha.save()
    captcha.created_at -= relativedelta.relativedelta(minutes=5)
    captcha.save()

    response = self.client.get(reverse("protected-view"), HTTP_X_CAPTCHA_UUID=captcha.uuid, HTTP_X_CAPTCHA_SECRET="abc")
    self.assertTrue(response.status_code == 400)
