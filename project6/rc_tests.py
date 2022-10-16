import unittest
import sys
sys.path.insert(1, '../')
from main import Family

class Test(unittest.TestCase):

    def test_US13_one(self):
        #valid
        filename = "../../data/US13/US13_one.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions == [])

    def test_US13_two(self):
        #kid born just before another
        filename = "../../data/US13/US13_two.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions != [])

    def test_US13_three(self):
        #kid born just after another
        filename = "../../data/US13/US13_three.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions != [])

    def test_US13_four(self):
        #large spacing
        filename = "../../data/US13/US13_four.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions == [])

    def test_US13_five(self):
        #kids close together
        filename = "../../data/US13/US13_five.ged"
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions != [])

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