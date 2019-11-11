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

def len_line(x,y):
    length=(x**2 + y**2)**(1/2)
    return length

x_1 = number_validator("Введіть абсцису точки А: ")
y_1 = number_validator("Введіть ординатуі точки А: ")
x_2 = number_validator("Введіть абсцису точки В: ")
y_2 = number_validator("Введіть ординату точки В: ")

if len_line(x_1,y_1) > len_line(x_2,y_2) :
    print("Точка В лежить ближче до початку координат")
elif len_line(x_1,y_1) < len_line(x_2,y_2):
    print("Точка А лежить ближче до початку координат")
else:
    print("Відстань від точок до початку координат рівні")