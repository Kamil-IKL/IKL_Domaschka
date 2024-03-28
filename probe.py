# Создайте функцию, которая отвечает на вопрос «Вы играете на банджо?».
# Если ваше имя начинается с буквы «R» или строчной «r», вы играете на банджо!
#
# Функция принимает имя в качестве единственного аргумента и возвращает одну из следующих строк:
#
# name + " plays banjo"
# name + " does not play banjo"
# Указанные имена всегда являются допустимыми строками.

def are_you_playing_banjo(name):
    # for i in name:
    #     if i == 'R' or i == 'r':
    #         print(f'{name} play the banjo.')
    #     pass
    # # print(f'{name} does not play banjo.')
    # return

    # print(type(name))
    if name[0] == 'R' or name[0] == 'r':
        print(f'{name} play the banjo.')
    else:
        print(f'{name} does not play banjo.')
    # return name

are_you_playing_banjo('Rim')
are_you_playing_banjo('rom')
are_you_playing_banjo('Irina')




