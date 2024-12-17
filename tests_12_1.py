import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj = runner.Runner('One')
        for _ in range(10):
            obj.walk()
        self.assertEqual(obj.distance,50)
        print('OK1')

    def test_run(self):
        obj = runner.Runner('Two')
        for _ in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)
        print('OK2')

    def test_challenge(self):
        obj1 = runner.Runner('Red')
        obj2 = runner.Runner('Yellow')
        for _ in range(10):
            obj1.run()
            obj1.walk()
            obj2.run()
            obj2.walk()
            self.assertNotEqual(obj1.distance, obj2.distance)
        print('OK3')