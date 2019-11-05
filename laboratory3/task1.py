import re
print("Борисенко Богдан Русланович \nЛабораторна робота №3 \nВаріант №2")
def ex1():
    text=input('Введіть текст : ')
    text=re.split('(\W+)',text)
    Result=[]
    for word in text :
        if re.search('\d+',word):
            pass
        else:
            if len(word)==5 :
                word=word[:3]+'xz'
        Result.append(word)
    print("Новий текст : "+ ''.join(Result))
ex1()
while True:
    answer = input("Для того щоб вийти введіть exit, для того щоб продовжити натисніть Enter ")
    if answer == "exit":
        break
    elif answer == "" :
        ex1()

    else :
        print('Ви зробили щось інше, а не ввели exit або натиснули Enter')