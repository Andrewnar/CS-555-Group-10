import unittest
import sys
sys.path.insert(1, '../')
from main import Family

class Test(unittest.TestCase):

    def test_US17_US18_one(self):
        filename = "../data/US17-18/US17-18_good.ged"
        fam = Family(filename)
        fam.create_family(filename)
        
        self.assertTrue(fam.exceptions == [])

    def test_US17_one(self):
        filename = "../data/US17/US17_bad.ged"
        fam = Family(filename)
        fam.create_family(filename)
        # print(fam)
        self.assertTrue(fam.exceptions != [])

    def test_US18_one(self):
        filename = "../data/US18/US18_bad.ged"
        fam = Family(filename)
        fam.create_family(filename)
        # print(fam)
        self.assertTrue(fam.exceptions != [])

if __name__ == '__main__':
    unittest.main()