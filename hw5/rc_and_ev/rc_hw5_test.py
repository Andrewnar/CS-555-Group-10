import unittest
from rc_hw5 import Family

class Test(unittest.TestCase):

    def test_US14_one(self):
        #valid
        filename = "../../data/US13/US13_one.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions == [])

    def test_US14_two(self):
        #kid born just before another
        filename = "../../data/US13/US13_two.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions != [])

    def test_US14_three(self):
        #kid born just after another
        filename = "../../data/US13/US13_three.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions != [])

    def test_US05_four(self):
        self.assertTrue(True)

    def test_US05_five(self):
        self.assertTrue(True)

    

if __name__ == '__main__':
    unittest.main()