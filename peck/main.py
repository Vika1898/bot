print("Pandemonica, The Tired Demon: Меня зовут Пандемоника, адская служба поддержки, чем могу служить?")
answer = input('<<Мы можем выяснить это у меня дома>> (a), <<Может я послужу тебе вместо этого?>> (b): ')
a = 'a'
b = 'b'
if answer == a:
    print('Ты думал, что покинешь ад живым? Как бредово.')
    print('<BAD END>')
    exit(0)
elif answer == b:
    print('Как мило с твоей стороны. Я бы не отказалась от кофе. Я сама не своя без него.')
    print('<SUCCESS>')
print('Вы перешли на следующий уровень. Воспользуйтесь советом')

advice = input("Напиши ответ: ") #при прохождении игры можно выбрать совет
if advice == 'совет':
    print('Pandemonica, The Tired Demon: Вы заметили, как много ходов занимает изучение Ада? В Аду если закончатся ходы - вы умрёте. Будьте внимательнее.')
else:
print('Pandemonica, The Tired Demon: Ничего не знаю. Иди дальше.')
skip = input('Введи "пройти", чтобы пройти головоломку: ')
if skip == 'пройти':
    print('Pandemonica, The Tired Demon: Отлично. Спасибо, что перешли на службу поддержки Ада. Как бы вы оценили работу по шкале от 1 до 10?')
    numbr = int(input('Введи число: '))
    if numbr in range(1, 10):
        print('Pandemonica, The Tired Demon: Хорошо, спасибо за оценку.')
    elif numbr == 10:
        print('Pandemonica, The Tired Demon: Вау! Никогда не получала десять раньше...')
    print('Pandemonica, The Tired Demon: Думаю, в ближайшее время врата не откроются. Чтобы убить время я загадаю тебе число от 1 до 9, а ты попытайся отгадать. Всё просто.')
    import random
    rnumber = (random.randint(1, 9))
    print('Pandemonica, The Tired Demon: Число есть. Теперь отгадывай.')
    answer = int(input('Введи ответ: '))
    print('Это было число', rnumber)
    if answer == rnumber:
        print('Pandemonica, The Tired Demon: Отлично! Ты угадал.')
    else:
        print('Pandemonica, The Tired Demon: Оу? Я не говорила? Ошибка - означает смерть. Ничего личного.')
        print('<BAD END>')
