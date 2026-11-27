import random


secret = random.randint(1, 100)
attempts = 0


print("Я загадал число от 1 до 100. Попробуй угадать!")


while True:


    user_input = input("Твоё предложение: ")


    if not user_input.isdigit():
        print("Пожалуйста, введите только целые числа.")
        continue


    guess = int(user_input)
    attempts += 1



    if guess < secret:
        print("БОЛЬШЕ")
    elif guess > secret:
        print("МЕНЬШЕ")
    else:
        print(f"Поздравляю! Ты угадал число {secret} за {attempts} попыток.")
