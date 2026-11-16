def main():
    books = []

    while True:
        print("\n=== ЧИТАТЕЛЬСКИЙ ДНЕВНИК ===")
        print("1 - добавить книгу")
        print("2 - показать все книги")
        print("3 - показать последние 5 прочитанных")
        print("4 - изменить название по номеру")
        print("5 - поиск по названию")
        print("6 - статистика")
        print("0 - выход")


        c = input("Выбор: ").strip()


        if c == "1":
            t = input("Название: ").strip()
            if not t:
                print("Ошибка: пустое название.")
            else:
                books.append(t)
                print("Добавлено.")


        elif c == "2":
            if not books:
                print("Дневник пуст.")
            else:
                for i, b in enumerate(books, 1):
                    print(f"{i}. {b}")


        elif c == "3":
            if not books:
                print("Дневник пуст.")
            else:
                start = max(0, len(books) - 5)
                for i in range(start, len(books)):
                    print(f"{i+1}. {books[i]}")


        elif c == "4":
            if not books:
                print("Дневник пуст.")
                continue
            n = input("Номер книги: ").strip()
            if not n.isdigit ():
                print("Ошибка: нужен номер.")
                continue
            n = int(n)
            if n < 1 or n > len(books):
                print("Ошибка: нет такой книги.")
                continue
            t = input("Новое название: ").strip()
            if not t:
                print("Ошибка: пустое название.")
                continue
            books[n-1] = t
            print("Изменено.")


        elif c == "5":
            if not books:
                print("Дневник пуст.")
                continue
            q = input("Поиск:").strip().lower()
            found = False
            for i, b in enumerate(books, 1):
                if q in b.lower():
                    print(f"{i}. {b}")
                    found = True
            if not found:
                print("Ничего не найдено.")


        elif c == "6":
            if not books:
                print("Дневниек пуст.")
                continue
            print(f"Всего: {len(books)}")
            print(f"Первая: {books[0]}")
            print(f"Последняя: {books[-1]}")


        elif c == "0":
            print("До встречи!")
            break

        else:
            print("Неверный пункт меню.")




if __name__ == "__main__":
    main()
