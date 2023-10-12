from django.test import TestCase

# 继承Django中的测试模块 即unittest.TestCase的子类django.test.TestCase
class TestExample(TestCase):
    def test_case(self):
        def calculate(num1, num2):
            return sum([num1, num2]), num1 + num2
        self.assertEqual(calculate(11,22)[0], 33)

