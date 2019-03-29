import unittest
from Base.BaseHttp2 import Login2

class LLL2(unittest.TestCase):
    def setUp(self):
        print("start")
        self.operation = Login2()

    def test_login2(self):
        self.operation.requset_get()

    def tearDown(self):
        print("end")

if __name__ == '__main__':
    unittest.main()