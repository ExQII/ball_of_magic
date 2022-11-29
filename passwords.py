import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
quantity = input('Какое нужно количество паролей?\n')
lenn = input('Какова должна быть длина пароля?\n')
digits_on = input('Должен ли пароль включать цифры? да или нет\n')
uppercase_letters_on = input('Должен ли пароль включать заглавные буквы? да или нет\n')
lowercase_letters_on = input('Должен ли пароль включать строчные буквы? да или нет\n')
symbols = input('Включать ли символы: "!#$%&*+-=?@^_" да или нет\n')
odnozn = input('Должен ли пароль исключать неоднозначные символы: "il1Lo0O" да или нет\n')
if digits_on == 'да':
    chars += digits
if uppercase_letters_on == 'да':
    chars += uppercase_letters
if lowercase_letters_on == 'да':
    chars += lowercase_letters
if symbols == 'да':
    chars += punctuation
if odnozn == 'да':
    for c in 'il1Lo0O':
        chars.replace(c, '')

def generate_password(lenght, chars):
    mylist = list(chars)
    generate = ''
    for i in range(int(lenght)):
        generate += random.choice(mylist)
    print(generate)

generate_password(lenn, chars)

for _ in range(int(quantity) - 1):
    generate_password(lenn, chars)




