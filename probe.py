# Создайте функцию, которая отвечает на вопрос «Вы играете на банджо?».
# Если ваше имя начинается с буквы «R» или строчной «r», вы играете на банджо!
#
# Функция принимает имя в качестве единственного аргумента и возвращает одну из следующих строк:
#
# name + " plays banjo"
# name + " does not play banjo"
# Указанные имена всегда являются допустимыми строками.

def are_you_playing_banjo(name):
    for i in name:
        if i == 'R' or i == 'r':
            print(f'{name} play the banjo.')
        pass
    #    return
    print(f'{name} does not play banjo.')
    return


are_you_playing_banjo('Ri')
are_you_playing_banjo('ra')
are_you_playing_banjo('Kamil')





