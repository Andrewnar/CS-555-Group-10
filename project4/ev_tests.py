import unittest
from project4 import Family

class Test(unittest.TestCase):

    def test_US07_one(self):
        successful = True
        try:
            filename = "../data/US07/US07_one.ged"
            fam = Family(filename)
            fam.create_family(filename)
        except Exception:
            successful = False
        self.assertTrue(successful)

    def test_US07_two(self):
        filename = "../data/US07/US07_two.ged"
        fam = Family(filename)
        self.assertRaises(Exception, fam.create_family, filename)

    def test_US07_three(self):
        successful = True
        try:
            filename = "../data/US07/US07_three.ged"
            fam = Family(filename)
            fam.create_family(filename)
        except Exception:
            successful = False
        self.assertTrue(successful)

    def test_US07_four(self):
        filename = "../data/US07/US07_four.ged"
        fam = Family(filename)
        self.assertRaises(Exception, fam.create_family, filename)

    def test_US07_five(self):
        filename = "../data/US07/US07_five.ged"
        fam = Family(filename)
        self.assertRaises(Exception, fam.create_family, filename)  

    def test_US08_one(self):
        successful = True
        try:
            filename = "../data/US08/US08_one.ged"
            fam = Family(filename)
            fam.create_family(filename)
        except Exception:
            successful = False
        self.assertTrue(successful)

    def test_US08_two(self):
        filename = "../data/US08/US08_two.ged"
        fam = Family(filename)
        self.assertRaises(Exception, fam.create_family, filename)

    def test_US08_three(self):
        filename = "../data/US08/US08_three.ged"
        fam = Family(filename)
        self.assertRaises(Exception, fam.create_family, filename)

    def test_US08_four(self):
        filename = "../data/US08/US08_four.ged"
        fam = Family(filename)
        self.assertRaises(Exception, fam.create_family, filename)

    def test_US08_five(self):
        successful = True
        try:
            filename = "../data/US08/US08_five.ged"
            fam = Family(filename)
            fam.create_family(filename)
        except Exception:
            successful = False
        self.assertTrue(successful) 

if __name__ == '__main__':
    unittest.main()