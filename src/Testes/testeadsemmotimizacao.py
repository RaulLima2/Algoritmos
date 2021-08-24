import unittest
import time
from memory_profiler import profile
from code import fibonacidinamico

class TestDinamico(unittest.TestCase):
    testetamanhoum = 10
    testetamanhodois = 20
    testetamanhotres = 30

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        time_run = time.time() - self.startTime
        print("{time_run}".format(time_run=time_run))

    @profile
    def testum(self):
        time.sleep(0)
        fib = fibonacidinamico(self.testetamanhoum)
        print(fib)

    @profile
    def testdois(self):
        time.sleep(1)
        fib = fibonacidinamico(self.testetamanhodois)
        print(fib)
    
    @profile
    def test_sortmedio(self):
        time.sleep(2)
        fib = fibonacidinamico(self.testetamanhotres)
        print(fib)
    

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDinamico)
    unittest.TextTestRunner(verbosity=0).run(suite)