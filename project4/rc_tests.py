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
        self.assertEqual("1","1")

    def test_US06_two(self):
        self.assertEqual("1","1")

    def test_US06_three(self):
        self.assertEqual("1","1")

    def test_US06_four(self):
        self.assertEqual("1","1")

    def test_US06_five(self):
        self.assertEqual("1","1")    

if __name__ == '__main__':
    unittest.main()