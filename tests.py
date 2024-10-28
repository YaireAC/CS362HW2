import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):

    def test_case_1(self):
        contrived_func(-3)

    def test_case_2(self):
        contrived_func(-2)

    def test_case_3(self):
        contrived_func(8)

    def test_case_4(self):
        contrived_func(11)

    def test_case_5(self):
        contrived_func(18)

    def test_case_6(self):
        contrived_func(21)

    def test_case_7(self):
        contrived_func(22)

    def test_case_8(self):
        contrived_func(17)


if __name__ == '__main__':
    unittest.main()
