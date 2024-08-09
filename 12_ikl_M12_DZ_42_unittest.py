import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj_1 = runner.Runner("VALERA")
        for i in range(10):
            obj_1.walk()
            # print(obj_1.distance) # для проверки результата
        self.assertEqual(obj_1.distance, 50)

    def test_run(self):
        obj_2 = runner.Runner('Leonid')
        for i in range(10):
            obj_2.run()
            # print(obj_2.distance) # для проверки результата
        self.assertEqual(obj_2.distance, 100)

    def test_challenge(self):
        obj_1 = runner.Runner("VALERA")
        obj_2 = runner.Runner('Leonid')
        for i in range(10):
            obj_1.walk()
            obj_2.run()
            print(obj_1.distance, obj_2.distance)  # для проверки результата
        self.assertNotEqual(obj_1.distance, obj_2.distance)


if __name__ == '__main__':
    unittest.main()
