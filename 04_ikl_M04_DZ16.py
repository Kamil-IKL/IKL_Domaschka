def test_function():
    print('Я в области видимости функции test_function ')

    def inner_function():
    #    print('Я в области видимости функции  inner_function')
        print('Я тоже... в области видимости функции test_function')

    inner_function()

test_function()
# inner_function() - Пайтон ее даже не видит, потому, что ее нет в глобальном пространстве

