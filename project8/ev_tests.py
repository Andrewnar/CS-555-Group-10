import unittest
import sys
sys.path.insert(1, '../')
from main import Family

class Test(unittest.TestCase):

    def test_US15_one(self):
        filename = "../data/US23/US23_one.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions == [])

    def test_US15_two(self):
        filename = "../data/US23/US23_two.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions != [])

    def test_US16_one(self):
        filename = "../data/US24/US24_one.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions == [])

    def test_US16_two(self):
        filename = "../data/US24/US24_two.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions != [])

if __name__ == '__main__':
    unittest.main()