from django.conf import settings
from django.utils.translation import ugettext as _
from rest_framework.request import Request
import importlib

def get_settings(string="REST_FRAMEWORK_CAPTCHA"):
  return getattr(settings, string, {})

def import_from_string(val):
  try:
    # Nod to tastypie's use of importlib.
    parts = val.split('.')
    module_path, class_name = '.'.join(parts[:-1]), parts[-1]
    module = importlib.import_module(module_path)
    return getattr(module, class_name)
  except ImportError as e:
    msg = "Could not import '%s' for setting. %s: %s." % (val, e.__class__.__name__, e)
    raise ImportError(msg)

def get_request_from_args(*args):
  for arg in args:
    if type(arg) is Request:
      return arg

  return None
