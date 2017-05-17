from django.test import TestCase
from rest_framework_captcha.generators import default

class DefaultGeneratorTestCase(TestCase):
  def test_default_generator_returns_6_char_string(self):
    self.assertTrue(len(default()) == 6)
