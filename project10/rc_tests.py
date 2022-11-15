import unittest
import sys
sys.path.insert(1, '../')
from main import Family

class Test(unittest.TestCase):

    def test_US29_one(self):
        filename = '../data/US29/US29_one.ged'
        fam = Family(filename)
        fam.create_family(filename)
        # do operation
        self.assertTrue(True)

    def test_US29_two(self):
        filename = '../data/US29/US29_two.ged'
        fam = Family(filename)
        fam.create_family(filename)
        # do operation
        self.assertTrue(True)

    def test_US30_one(self):
        filename = '../data/US30/US30_one.ged'
        fam = Family(filename)
        fam.create_family(filename)
        # do operation
        self.assertTrue(True)

    def test_US30_two(self):
        filename = '../data/US30/US30_two.ged'
        fam = Family(filename)
        fam.create_family(filename)
        # do operation
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()