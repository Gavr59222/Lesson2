while True:
    var_str = input('Пожалуйста введите несколько слов разделяя их пробелами: ')
    if len(var_str) < 3 or var_str.count(' ') < 1:
        print('Неправильно введенные данные. Попробуйте еще раз')
        continue

    break

for idx, word in enumerate(var_str.split()):
    print(idx + 1, (word, word[:11])[len(word) > 10])
