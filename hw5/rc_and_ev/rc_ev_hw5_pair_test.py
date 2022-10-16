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

    def test_US14_four(self):
        filename = "../../data/US14/US14_four.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions == [])

    def test_US14_five(self):
        filename = "../../data/US14/US14_five.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions != [])

    

if __name__ == '__main__':
    unittest.main()