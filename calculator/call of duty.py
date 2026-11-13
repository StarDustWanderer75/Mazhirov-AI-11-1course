print("=== Калькулятор покупок ===")
print("Операции:")
print("1 - сложение      (стоимость + доставка)")
print("2 - вычитание     (сколько останется от денег)")
print("3 - умножение     (цена x количество)")
print("4 - деление       (цена за штуку)")
print("5 - возведение в степень")
print("6 - остаток от деления (сдача при распределении)")
print("7 - целочисленное деление (сколько полных комплектов)")
print("0 - выход")
print()


run = True


while run:
    choice = input("Выберите операцию (1-7, 0 для выхода): ")


    if choice == "0":
        print("Программа звершина. До свидания!")
        run = False 
    elif choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7":

        a = float(input("Введите первое число:"))
        b = float(input("Введите второе число:"))

        if choice == "1":
            result = a + b
            print("Сумма =", result)
        elif choice == "2":
            result = a - b
            print("Разность =", result)
        elif choice == "3":
            print = a * b
            print("Произведение =", result)
        elif choice == "4":
            if b == 0:
                print("Ошибка: деление на ноль невозможно!")
            else:
                result = a / b
                print("Частное =", result)
        elif choice == "5":
            result = a ** b
            print("Степень =", result)
        elif choice == "6":
            if b == "0":
                print("Ошибка: деление на ноль невозможно!")
            else:
                result = a % b
                print("Остаток =", result)
        elif choice == "7":
            if b == 0:
                print("Ошибка: деление на ноль невозможно!")
            else:
                result = a // b
                print("Целочисленное деление =", result)

        if choice != "4" and choice != "6" and choice != "7" or (b != 0 and (choice == "4" or choice == "6" or choice == "7")):
            if result > 5000:
                print("Крупная покупка!")
    else:
        print("Нет такой операции! Попробуйте ещё раз.")


    print()
    