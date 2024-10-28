import unittest
from contrived_func import contrived_func

class TestContrivedFunc(unittest.TestCase):
   
    def test_case_1(self):
        contrived_func(-3) 

    def test_case_2(self):
        contrived_func(5)   

    def test_case_3(self):
        contrived_func(20)  

    def test_case_4(self):
        contrived_func(10) 

    def test_case_5(self):
        contrived_func(7) 

    def test_case_6(self):
        contrived_func(2)   

    def test_case_7(self):
        contrived_func(-1) 

    def test_case_8(self):
        contrived_func(3)   
       
    def test_case_9(self):
        contrived_func(200)

    def test_case_11(self):
        contrived_func(50)
       
    def test_case_11(self):
        contrived_func(3)

   def test_case_11(self):
        contrived_func(18)

   def test_case_11(self):
        contrived_func(24)

   def test_case_11(self):
        contrived_func(8)

if __name__ == '__main__':
    unittest.main()
