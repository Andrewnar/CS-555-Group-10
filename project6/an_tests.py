import unittest
import sys
sys.path.insert(1, '../')
from main import Family

class Test(unittest.TestCase):

    def test_US09_US10_one(self):
        filename = "../data/US09-10/US09-10_good.ged"
        fam = Family(filename)
        fam.create_family(filename)
        
        self.assertTrue(fam.exceptions == [])

    def test_US09_one(self):
        filename = "../data/US09/US09_bad.ged"
        fam = Family(filename)
        fam.create_family(filename)
        print(fam)
        self.assertTrue(fam.exceptions != [])

    def test_US10_one(self):
        filename = "../data/US10/US10_bad.ged"
        fam = Family(filename)
        fam.create_family(filename)
        print(fam)
        self.assertTrue(fam.exceptions != [])

if __name__ == '__main__':
    unittest.main()