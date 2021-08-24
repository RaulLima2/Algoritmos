import time
import unittest
from code import fibonacidinamicootimizado
from memory_profiler import profile

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
        fib = fibonacidinamicootimizado(self.testetamanhoum)
        print(fib)

    @profile
    def testdois(self):
        time.sleep(1)
        fib = fibonacidinamicootimizado(self.testetamanhodois)
        print(fib)
    
    @profile
    def test_sortmedio(self):
        time.sleep(2)
        fib = fibonacidinamicootimizado(self.testetamanhotres)
        print(fib)
    

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDinamico)
    unittest.TextTestRunner(verbosity=0).run(suite)