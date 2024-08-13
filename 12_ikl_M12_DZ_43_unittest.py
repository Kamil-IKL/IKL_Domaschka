import runner_and_tournament
import unittest
import pprint


# Класс TournamentTest для тестирования турнира
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # словарь для хранения результатов тестов
        cls.all_results = {}

    def setUp(self):
        # создаю бегунов
        self.runner_usain = runner_and_tournament.Runner('Усейн', 10)
        self.runner_andrey = runner_and_tournament.Runner('Андрей', 9)
        self.runner_nik = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print('\nВсе результаты:')
        for name, result in cls.all_results.items():  # метод ".items()" для вывода пары "ключ-значение" словаря в столбец
            print(f'\n{name}: ')
            for pacte, runner in result.items():  # раскрываю словарь result
                print(f'{pacte} место: {runner}')
        """
        Это мне для изучения, как вместо строк 22-25 можно написать в одну строку 
        (пересмотреть Модуль 9. Списковые сборки)
        """
        # _ = [print('забег:', x, ' - ', k, 'место:', z) for x, y in cls.all_results.items() for k, z in y.items()]

    # Первый забег на 90м.: Усейн и Ник
    def test_usain_nik(self):
        tournament_90 = runner_and_tournament.Tournament(90, self.runner_usain, self.runner_nik)
        results = tournament_90.start()
        self.all_results['Усейн и Ник'] = results
        self.assertTrue(results[2] == 'Ник')

    # Второй забег на 90м.: Андрей и Ник
    def test_andrey_nik(self):
        tournament_90 = runner_and_tournament.Tournament(90, self.runner_andrey, self.runner_nik)
        results = tournament_90.start()
        self.all_results['Андрей и Ник'] = results
        self.assertTrue(results[2] == 'Ник')

    # Третий забег на 90м.: Усейн, Андрей и Ник
    def test_usain_andrey_nik(self):
        tournament_90 = runner_and_tournament.Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nik)
        results = tournament_90.start()
        self.all_results['Усейн, Андрей и Ник'] = results
        self.assertTrue(results[3] == 'Ник')


if __name__ == '__main__':
    unittest.main()
