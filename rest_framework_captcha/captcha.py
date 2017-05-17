from captcha.image import ImageCaptcha
from rest_framework_captcha import helpers
from rest_framework_captcha import models

class Captcha():
  def __init__(self, secret_generator="default"):
    secret_generator_name = helpers.get_settings().get("SECRET_GENERATOR", {}).get(secret_generator, "rest_framework_captcha.generators.default")
    self.secret_generator = helpers.import_from_string(secret_generator_name)

    self._generate()

  def _generate(self):
    self._generate_secret()
    self._create_model()

    image = ImageCaptcha()
    data = image.generate(self.secret)
    self.image = data

  def _generate_secret(self):
    self.secret = self.secret_generator()

  def _create_model(self):
    self.model_instance = models.Captcha(secret=self.secret)
    self.model_instance.save()
