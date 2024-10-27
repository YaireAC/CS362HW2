import unittest
from contrived_func import contrived_func

class TestContrivedFunc(unittest.TestCase):

    def test_case_1(self):
        contrived_func(10)  # a=True

    def test_case_2(self):
        contrived_func(-10)  # a=False

    def test_case_3(self):
        contrived_func(2)  # b=True

    def test_case_4(self):
        contrived_func(3)  # b=False

    def test_case_5(self):
        contrived_func(200)  # c=False

    def test_case_6(self):
        contrived_func(-2)  # d=True

    def test_case_7(self):
        contrived_func(1)  # d=False

    def test_case_8(self):
        contrived_func(50)  # b=False and c=False

    def test_case_9(self):
        contrived_func(4)  # Combined condition test

    def test_case_10(self):
        contrived_func(8)  # Combined condition test

    def test_case_11(self):
        contrived_func(6)  # Combined condition test

    def test_case_12(self):
        contrived_func(-1)  # Combined condition test

    def test_case_13(self):
        contrived_func(5)  # Combined condition test

if __name__ == '__main__':
    unittest.main()
