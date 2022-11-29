import random
def is_valid(n):
    if 1 <= int(n) <= 100:
        return True
    else:
        return False

def guess():
    while True:
        a = input()
        is_valid(a)
        if is_valid(a):
            return int(a)
        else:
            print('А может все-таки Сашенька введет целое число от 1 до 100?')

def game():
    print('Добро пожаловать в числовую угадайку, миссис Сашенька')
    while True:
        print('Укажи границы чисел, в которых будешь угадывать\nВ пределах от 1 до 100')
        x, y = guess(), guess()
        if x > y:
            x, y = y, x
        print('Введи число от', x, 'до', y, '\n')
        compare_num(x, y)

def compare_num(left, right):
    num = random.randint(left, right)
    total = 0
    while True:
        n = guess()
        if n < num:
            total += 1
            print('Число Сашеньки меньше загаданного, попробуй еще разок')
        elif n > num:
            total += 1
            print('Число Сашеньки больше загаданного, попробуй еще разок')
        else:
            total += 1
            print('Сашенька угадала,она у Максимки самая умная!!!')
            print('Сашенька справилась за:', total, 'попыток')
            print('Спасибо, что играла в числовую угадайку. Ты самое милое солнышко :)')
            print('Хочешь сыграть ещё? "да" или "нет"')
            otvet = input()
            if otvet == 'нет':
                print('Ладно, гуляй...')
                break
            else:
                while otvet == 'да':
                    game()



game()
