def ex1():
    lower_bound_of_sum=1
    while 1:
        try:
            upper_bound_of_sum=int(input("Введіть верхню межу суми : "))+1
            break
        except ValueError:
            print("Ви помилилися і ввели не число :)")
    while 1 :
        try:
            variable=int(input("Введіть число замість змінної x : "))
            break
        except ValueError:
            print("Ви помилилися і ввели не число :)")
    result=0
    while variable==0 :
        try:
            variable = float(input("Введіть число відмінне від 0 : "))
            break
        except ValueError:
                print("Ви помилилися і ввели не число :)")
    for lower_bound_of_sum in range (lower_bound_of_sum, upper_bound_of_sum):
        result+=lower_bound_of_sum/(variable**lower_bound_of_sum)
        lower_bound_of_sum+=1
    print("Сумою є число " + str(result))