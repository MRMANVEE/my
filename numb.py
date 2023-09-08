import random

def generate_random_mobile_number():
    country_code = "+91 "
    number_length = 10

    random_digits = [random.choice("0123456789") for _ in range(number_length)]
    random_number = ''.join(random_digits)

    return country_code + random_number

num = generate_random_mobile_number()
print("Random Mobile Number : ", num)