import unittest
import sys
sys.path.insert(1, '../')
from main import Family

class Test(unittest.TestCase):

    # valid family
    def test_US21_one(self):
        filename = "../data/US21/US21_one.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions == [])

    # invalid marriage
    def test_US21_two(self):
        filename = "../data/US21/US21_two.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions != [])

    # cannot fail without breaking code -- will pass
    def test_US22_one(self):
        filename = "../data/US22/US22_one.ged"
        family = Family(filename)
        family.create_family(filename)
        self.assertTrue(family.exceptions == [])

if __name__ == '__main__':
    unittest.main()