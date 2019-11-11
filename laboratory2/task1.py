'''
Написати програму, що обчислює
суму членів послідовності (i/x^i) з i по n, i=1
'''

import re

re_number = re.compile("^[-+]?\d+\.?\d*$")
re_integer = re.compile("^\d+$")

def validator(pattern,promt):
    text=input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def number_validator(promt):
    number=float(validator(re_number, promt))
    return number

def integer_validator(promt):
    number=int(validator(re_integer, promt))
    return number

lower_bound_of_sum=1
upper_bound_of_sum=integer_validator("Введіть верхню межу суми : ")+1
variable=number_validator("Введіть число замість змінної x : ")
result=0
while variable==0 :
    variable = number_validator("Введіть число замість змінної x : ")
for bound in range (lower_bound_of_sum, upper_bound_of_sum):
    result+=bound/(variable**bound)
print("Сумою є число " + str(result))