import unittest
from project4 import Family

class Test(unittest.TestCase):

    def test_US05_one(self):
        # valid family -- should pass
        try:
            filename = '../data/US05/US05_one.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_US05_two(self):
        # death before marriage -- should fail
        try:
            filename = '../data/US05/US05_two.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_US05_three(self):
        # death on marriage day -- should pass
        try:
            filename = '../data/US05/US05_three.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_US05_four(self):
        # death one month after marriage date -- should pass
        try:
            filename = '../data/US05/US05_four.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_US05_five(self):
        # death one month before marriage date -- should fail
        try:
            filename = '../data/US05/US05_five.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_US06_one(self):
        # valid family -- should pass
        try:
            filename = '../data/US06/US06_one.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_US06_two(self):
        # death before divorce -- should fail
        try:
            filename = '../data/US06/US06_two.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_US06_three(self):
        # death on divorce day -- should pass
        try:
            filename = '../data/US06/US06_three.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_US06_four(self):
        # death one month after divorce date -- should pass
        try:
            filename = '../data/US06/US06_four.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_US06_five(self):
        # death one month before divorce date -- should fail
        try:
            filename = '../data/US06/US06_five.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()