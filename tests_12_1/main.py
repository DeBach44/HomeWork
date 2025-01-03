import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runer = runner.Runner('Denis')
        for _ in range(10): runer.walk()
        self.assertEqual(runer.distance,50)

    def test_run(self):
        runer = runner.Runner('Denis')
        for _ in range(10): runer.run()
        self.assertEqual(runer.distance,100)

    def test_challenge(self):
        runer_one = runner.Runner('Denis')
        runer_two = runner.Runner('Dmitriy')
        for _ in range(10): runer_one.walk()
        for _ in range(10): runer_two.run()
        self.assertNotEqual(runer_one.distance,runer_two.distance)

if __name__ == '__main__':
    unittest.main()