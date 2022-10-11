import unittest
from rc_ev_hw5_pair import Family

class Test(unittest.TestCase):

    def test_US14_one(self):
        filename = "../../data/US14/US14_one.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions == [])

    def test_US14_two(self):
        filename = "../../data/US14/US14_two.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions == [])

    def test_US14_three(self):
        filename = "../../data/US14/US14_three.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions != [])

    def test_US05_four(self):
        self.assertTrue(True)

    def test_US05_five(self):
        self.assertTrue(True)

    

if __name__ == '__main__':
    unittest.main()