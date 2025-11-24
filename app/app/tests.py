from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    def testCalc(self):
        res = calc.add(9, 10)
        self.assertEqual(res, 19)

    def testCalc1(self):
        res = calc.add(9, 90)
        self.assertEqual(res, 99)