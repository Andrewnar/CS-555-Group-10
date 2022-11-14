import unittest
import sys
sys.path.insert(1, '../')
from main import Family

class Test(unittest.TestCase):

    def test_US31_one(self):
        filename = '../data/US31/testfamily.ged'
        fam = Family(filename)
        fam.create_family(filename)
        result = fam.list_living_single()
        self.assertTrue(len(result) == 1)

    def test_US32_one(self):
        filename = '../data/US32/testfamily.ged'
        fam = Family(filename)
        fam.create_family(filename)
        result = fam.list_mult_births()
        self.assertTrue(len(result) == 7)

if __name__ == '__main__':
    unittest.main()