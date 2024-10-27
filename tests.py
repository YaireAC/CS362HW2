import unittest
from contrived_func import contrived_func

class TestContrivedFunc(unittest.TestCase):
   
    def test_case_1(self):
        contrived_func(-3)  # a=True, b=True, c=True, d=True

    def test_case_2(self):
        contrived_func(5)   # a=True, b=True, c=True, d=False

    def test_case_3(self):
        contrived_func(20)  # a=True, b=True, c=False, d=False

    def test_case_4(self):
        contrived_func(10)   # a=True, b=False, c=True, d=False

    def test_case_5(self):
        contrived_func(7)   # a=False, b=True, c=True, d=False

    def test_case_6(self):
        contrived_func(2)   # a=False, b=False, c=True, d=False

    def test_case_7(self):
        contrived_func(-1)  # a=False, b=True, c=False, d=True

    def test_case_8(self):
        contrived_func(3)   # a=False, b=False, c=False, d=False
       
    def test_case_9(self):
        contrived_func(200)

   def test_case_10(self):
        contrived_func(10)

    def test_case_10(self):
        contrived_func(50)

if __name__ == '__main__':
    unittest.main()
