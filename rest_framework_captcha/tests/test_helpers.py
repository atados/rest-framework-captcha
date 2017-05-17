from rest_framework_captcha.helpers import import_from_string
from django.test import TestCase

class TestImportFromString(TestCase):
  def test_import_from_string_raises_error(self):
    with self.assertRaises(ValueError):
      import_from_string("")

    with self.assertRaises(ImportError):
      import_from_string("inexistent.module")
