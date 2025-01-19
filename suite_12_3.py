import unittest
from tests_12_3 import RunnerTest as rt
from tests_12_3 import TournamentTest as tt

run_rt = unittest.TestSuite()
run_rt.addTest(unittest.TestLoader().loadTestsFromTestCase(rt))
tour_tt = unittest.TestSuite()
tour_tt.addTest(unittest.TestLoader().loadTestsFromTestCase(tt))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_rt)
runner.run(tour_tt)