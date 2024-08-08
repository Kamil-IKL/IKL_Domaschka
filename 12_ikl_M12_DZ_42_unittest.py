import runner
import unittest


class RunnerTest(unittest.TestCase):
    # def test_walk(self):
    #     obj_1 = runner.Runner("VALERA")
    #     for i in range(10):
    #         # obj = runner.Runner(f"VALERA_{i}")
    #         # print(obj)
    #         obj_1.walk()
    #         # print(obj_1.distance)
    #     self.assertEqual(obj_1.distance, 50)
        # pass
    #
    # def test_run(self):
    #     obj_2 = runner.Runner('Leonid')
    #     for i in range(10):
    #         obj_2.run()
    #         # print(obj_2.distance)
    #     self.assertEqual(obj_2.distance,100)
    #     # pass

    def test_challenge(self):
        obj_1 = runner.Runner("VALERA")
        # obj_2 = runner.Runner('Leonid')
        for i in range(10):
            obj_1.walk()
            obj_1.run()
            print(obj_1.distance)
        self.assertNotEqual(obj_1.distance, True  )
        obj_2 = runner.Runner('Leonid')
        for i in range(10):
            obj_2.walk()
            obj_2.run()
            print(obj_2.distance)
        self.assertNotEqual(obj_2.distance, False)


if __name__ == '__main__':
    unittest.main()
