import random
import string

def generate_otp(length = 6):
    charactors = string.digits
    return ''.join(random.choice(charactors) for _ in range(length))

otp = generate_otp()
print("Random OTP was Generated Successfully :", otp)