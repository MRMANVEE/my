import pyotp

num = input("Enter the Number :")

secrete_key = "JBSWY3DPEHPK3PXP"

totp = pyotp.TOTP(secrete_key)
otp = totp.now()
print(otp)