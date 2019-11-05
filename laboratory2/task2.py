def ex2():
    while 1:
        try:
            number = int(input("Введіть число з якого хочете видалити цифру : "))
            break
        except ValueError:
            print("Ви помилилися і ввели не число :)")
    while 1:
        try:
            delete_number = int(input("Введіть цифру яку ви хочете видалити з числа " + str(number) + " : "))
            break
        except ValueError:
            print("Ви помилилися і ввели не цифру :)")
    List = list(str(number))
    result = []
    if str(delete_number) not in List:
        print("Цифри " + str(delete_number) + " немає у числі " + str(number))
    for a in List:
        if str(delete_number) != a:
            result.append(a)
    print("Отримане число : "+"".join(result))