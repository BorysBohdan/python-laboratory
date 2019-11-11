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

lower_bound_of_sum=1

upper_bound_of_sum=int(float_greater_zero_validator("Введіть верхню межу суми : "))+1
variable=float_greater_zero_validator("Введіть число замість змінної x : ")
result=0
while variable==0 :
    variable = float_greater_zero_validator("Введіть число замість змінної x : ")
for bound in range (lower_bound_of_sum, upper_bound_of_sum):
    result+=bound/(variable**bound)
print("Сумою є число " + str(result))