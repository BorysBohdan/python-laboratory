import re

re_number = re.compile("^[-+]?\d+\.?\d*$")

def validator(pattern,promt):
    text=input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def float_greater_zero_validator(promt):
    number=float(validator(re_number, promt))
    return number

x = float_greater_zero_validator("Введіть число замість x : ")

if x >= 3:
    print("Результатом обчислення є число " + str((-x) ** 2 + 3 * x + 9))
else :
    print("Результатом обчислення є число " + str(1/(x**3-6)))