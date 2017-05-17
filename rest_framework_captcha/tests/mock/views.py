from rest_framework_captcha.decorators import protected_view
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
@protected_view
def protected_view(request):
  return Response({"message": "Hello, world!"})
