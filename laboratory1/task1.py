def exercise1():
    print("Обчислення відсотка одного числа від іншого")
    first_number = float(input("Введіть число для якого будемо обчислювати відсоток  : "))
    second_number = float(input("Введіть число відсоток від якого будемо обчислювати відсоток. : "))
    result = str(second_number/first_number*100)
    print("Відсоток числа " + str(second_number) + " від числа " + str(first_number) + " становить : " + result + " %")