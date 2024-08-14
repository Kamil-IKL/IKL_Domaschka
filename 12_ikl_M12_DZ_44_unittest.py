import unittest
import Test_runner
import Test_tournament


suiteST = unittest.TestSuite()
suiteST.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_runner.RunnerTest))
suiteST.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_tournament.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suiteST)



