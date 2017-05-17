from django.conf import settings
from django.utils.translation import ugettext as _


def get_settings(string="REST_FRAMEWORK_CAPTCHA"):
  return getattr(settings, string, {})
