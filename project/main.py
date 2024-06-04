import random


def gues_num(x=10):
    num = random.randint(1, x)
    count = 0
    print(f'Я задумал число от 1 до {x}. Сможешь ли ты его найти?')
    while True:
        count += 1
        gues = int(input('>>> '))
        if gues > num:
            print(f'Моё число меньше {gues}')
        elif gues < num:
            print(f"Мое число больше, чем {gues}")
        else:
            break
    print(f"Поздравляем, вы нашли его с {count} попыток.")

    return count


def gues_num_pc(x=10):
    input(f"Задумайте число от 1 до {x} и нажмите любую кнопку. Я найду >> ")
    count = 0
    _min = 1
    _max = x
    while True:
        count += 1
        if _min != _max:
            num = random.randint(_min, _max)
        else:
            num = _min
        answer = input(f"Вы угадали цифру {num}. Если верно - ( t ), если больше - ( + ), если меньше ( - ), введите >> ".lower())
        if answer == '+':
            _min = num + 1
        elif answer == '-':
            _max = num - 1
        elif answer == 't':
            break
    print(f"Я нашел это за {count} попыток")

    return count


def play(x=10):
    count_play = 0
    again = True
    while again:
        count_play += 1
        user_count = gues_num(x)
        pc_count = gues_num_pc(x)

        if user_count < pc_count:
            print(f"Ты выиграл")
        elif user_count > pc_count:
            print(f"Я выиграл")
        else:
            print(f"Счет равный")

        again = int(input(f"Поиграем еще раз? ОК (1), НЕТ (0)"))
    print(f"Спасибо за игру")

    return count_play


print(play(x=20))








