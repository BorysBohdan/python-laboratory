'''
Написати програму обчислення конкретної функції,
в залежності від введеного значення х.

f(x)={ -x^2 + 3x + 9, якщо x<=3
f(x)={ 1/(x^3 + 6), якщо якщо x>3

'''


import re

re_number = re.compile("^[-+]?\d+\.?\d*$")

def validator(pattern,promt):
    text=input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def number_validator(promt):
    number=float(validator(re_number, promt))
    return number

x = number_validator("Введіть число замість x : ")

if x >= 3:
    print("Результатом обчислення є число " + str((-x) ** 2 + 3 * x + 9))
else :
    print("Результатом обчислення є число " + str(1/(x**3-6)))