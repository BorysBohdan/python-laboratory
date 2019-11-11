import re

re_number = re.compile("^[-+]?\d+\.?\d*$")

def validator(pattern,promt):
    text=input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def float_greater_zero_validator(promt):
    number=float(validator(re_number, promt))
    while number<=0:
        number=float(validator(re_number, promt))
    return number
num1=float_greater_zero_validator("Введіть число для якого будемо обчислювати відсоток: ")
num2=float_greater_zero_validator("Введіть число відсоток від якого будемо обчислювати відсоток: ")
print("Відсоток числа " + str(num2) + " від числа " + str(num1) + " становить : " + str(num2/num1*100) + " %")