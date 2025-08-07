"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """test calc module"""

    def test_add_numbers(self):
        """test adding nums togehter"""
        res = calc.add(5,6)

        self.assertEqual(res,11)
    
    def test_subtract_number(self):

        "subtract nos"
        res=calc.subtract(10,15)
        self.assertEqual(res,5)

