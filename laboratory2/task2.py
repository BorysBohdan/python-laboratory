'''
Написати програму, що видаляє цифру з натурального числа
'''



import re

re_number = re.compile("^\d+$")
re_digit = re.compile("^\d$")

def validator(pattern,promt):
    text=input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def number_validator(promt):
    number=int(validator(re_number, promt))
    return number

def digit_validator(promt):
    number=int(validator(re_digit, promt))
    return number

number = number_validator("Введіть натуральне число з якого хочете видалити цифру : ")
delete_number = digit_validator("Введіть цифру яку ви хочете видалити з числа " + str(number) + " : ")
List = list(str(number))
result = []
if str(delete_number) not in List:
    print("Цифри " + str(delete_number) + " немає у числі " + str(number))
for number in List:
    if str(delete_number) != number:
        result.append(number)
print("Отримане число : "+ "".join(result))