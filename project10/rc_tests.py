import unittest
import sys
sys.path.insert(1, '../')
from main import Family

class Test(unittest.TestCase):

    def test_US29_one(self):
        filename = '../data/US29/US29_one.ged'
        fam = Family(filename)
        fam.create_family(filename)
        result = fam.list_deceased()
        self.assertTrue(len(result) == 2)

    def test_US29_two(self):
        filename = '../data/US29/US29_two.ged'
        fam = Family(filename)
        fam.create_family(filename)
        result = fam.list_deceased()
        self.assertTrue(len(result) == 0)

    def test_US30_one(self):
        filename = '../data/US30/US30_one.ged'
        fam = Family(filename)
        fam.create_family(filename)
        result = fam.list_living_married()
        self.assertTrue(len(result) == 19)

if __name__ == '__main__':
    unittest.main()