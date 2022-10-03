import unittest
from project4 import Family

class Test(unittest.TestCase):

    def test_US03_one(self):
        # Daisy has a death date 80 years after her birthday : pass
        try:
            filename = '../data/US03/US03_one.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions == [])
        except Exception:
            self.assertTrue(False)

    def test_US03_two(self):
        # Maisy death 10 years before birth : fail
        try:
            filename = '../data/US03/US03_two.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions != [])
        except Exception:
            self.assertTrue(False)

    def test_US03_three(self):
        # Maisy death on exact day of birth : pass
        try:
            filename = '../data/US03/US03_three.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions == [])
        except Exception:
            self.assertTrue(False)

    def test_US03_four(self):
        # Daisy and Jim both have death dates after their birthdays : pass
        try:
            filename = '../data/US03/US03_four.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions != [])
        except Exception:
            self.assertTrue(False)

    def test_US03_five(self):
        # Maisy death two years before birth date , Jenny four years before birth date: fail
        try:
            filename = '../data/US03/US03_five.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions != [])
        except Exception:
            self.assertTrue(False)

    def test_US04_one(self):
        # Daisy and Jim marriage comes before divorce : pass
        try:
            filename = '../data/US04/US04_one.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions == [])
        except Exception:
            self.assertTrue(False)

    def test_US04_two(self):
        #  Daisy and Jim marriage comes 2 years after divorce : fail
        try:
            filename = '../data/US04/US04_two.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions != [])
        except Exception:
            self.assertTrue(False)

    def test_US04_three(self):
        #  Daisy and Jim divorce happens 20 days after marriage : fail
        try:
            filename = '../data/US04/US04_three.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions != [])
        except Exception:
            self.assertTrue(False)

    def test_US04_four(self):
        # Daisy and Jim divorce 30 years after marriage : pass
        try:
            filename = '../data/US04/US04_four.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions == [])
        except Exception:
            self.assertTrue(False)

    def test_US04_five(self):
        # Daisy and Jim's divorce happens 20 years before marriage : fail
        try:
            filename = '../data/US04/US04_five.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.exceptions != [])
        except Exception:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()