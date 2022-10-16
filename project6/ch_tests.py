import unittest
import sys
sys.path.insert(1, '../')
from main import Family

class Test(unittest.TestCase):

    def test_US11_good(self):
        filename = "../data/US11/US11_good.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions == [])

    def test_US11_bad(self):
        filename = "../data/US11/US11_bad.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions != [])

    def test_US12_good(self):
        filename = "../data/US12/US12_good.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions == [])

    def test_US12_bad(self):
        filename = "../data/US12/US12_bad.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions != [])

if __name__ == '__main__':
    unittest.main()