import unittest
from project4 import Family

class Test(unittest.TestCase):

    def test_US01_one(self):
        try:
            filename = '../data/US01/US01_tests.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions != [])
        except Exception:
            self.assertTrue(False)

    def test_US01_two(self):
        try:
            filename = '../data/US01/US01_two.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions != [])
        except Exception:
            self.assertTrue(False)

    def test_US01_three(self):
        try:
            filename = '../data/US01/US01_three.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions != [])
        except Exception:
            self.assertTrue(False)

    def test_US01_four(self):
        try:
            filename = '../data/US01/US01_four.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions != [])
        except Exception:
            self.assertTrue(False)

    def test_US01_five(self):
        try:
            filename = '../data/US01/US01_five.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions == [])
        except Exception:
            self.assertTrue(False)

    def test_US02_one(self):
        try:
            filename = '../data/US02/US02_one.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions != [])
        except Exception:
            self.assertTrue(False)

    def test_US02_two(self):
        try:
            filename = '../data/US02/US02_two.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions != [])
        except Exception:
            self.assertTrue(False)

    def test_US02_three(self):
        try:
            filename = '../data/US02/US02_three.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions != [])
        except Exception:
            self.assertTrue(False)

    def test_US02_four(self):
        try:
            filename = '../data/US02/US02_four.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions == [])
        except Exception:
            self.assertTrue(False)

    def test_US02_five(self):
        try:
            filename = '../data/US02/US02_five.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions == [])
        except Exception:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()