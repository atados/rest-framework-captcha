from functools import wraps
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from rest_framework_captcha.models import Captcha
from rest_framework_captcha.helpers import get_settings, get_request_from_args
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

def protected_view(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    request = get_request_from_args(*args)

    uuid = request.META.get("HTTP_X_CAPTCHA_UUID", None)
    secret = request.META.get("HTTP_X_CAPTCHA_SECRET", None)
    time_limit = get_settings().get("EXPIRE_IN", 5*60)

    if not uuid or not secret:
      return Response({"message": "This view is protected by captcha. You have to set headers X-Captcha-UUID and X-Captcha-Secret with valid values."}, status=400)

    try:
      captcha = Captcha.objects.get(uuid=uuid, secret=secret, fresh=True, created_at__gte=timezone.now() - relativedelta(seconds=time_limit))
    except (Captcha.DoesNotExist, ValueError):
      return Response({"message": "Invalid/expired captcha or incorrect secret."}, status=400)

    captcha.fresh = False
    captcha.save()

    return func(request, *args, **kwargs)

  return wrapper
