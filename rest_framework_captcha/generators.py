import random
import string

def default():
  digits = string.ascii_letters + string.digits
  secret = ''.join(random.choice(digits) for i in range(6))

  return secret
