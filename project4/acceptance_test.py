import unittest
from project4 import Family

class Test(unittest.TestCase):

    #
    # ACCEPTANCE TEST CASES FOR ALL SPRINT 1 USER STORIES
    #

    #
    # US01
    #

    #
    # US02
    #

    #
    # US03
    #

    def test_US03_one(self):
        # Daisy has a death date 80 years after her birthday : pass
        try:
            filename = '../data/US03/US03_one.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_US03_two(self):
        # Maisy death 10 years before birth : fail
        try:
            filename = '../data/US03/US03_two.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_US03_three(self):
        # Maisy death on exact day of birth : pass
        try:
            filename = '../data/US03/US03_three.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_US03_four(self):
        # Daisy and Jim both have death dates after their birthdays : pass
        try:
            filename = '../data/US03/US03_four.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_US03_five(self):
        # Maisy death two years before birth date , Jenny four years before birth date: fail
        try:
            filename = '../data/US03/US03_five.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    #
    # US04
    #

    def test_US04_one(self):
        # Daisy and Jim marriage comes before divorce : pass
        try:
            filename = '../data/US04/US04_one.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_US04_two(self):
        #  Daisy and Jim marriage comes 2 years after divorce : fail
        try:
            filename = '../data/US04/US04_two.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_US04_three(self):
        #  Daisy and Jim divorce happens 20 days after marriage : fail
        try:
            filename = '../data/US04/US04_three.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_US04_four(self):
        # Daisy and Jim divorce 30 years after marriage : pass
        try:
            filename = '../data/US04/US04_four.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_US04_five(self):
        # Daisy and Jim's divorce happens 20 years before marriage : fail
        try:
            filename = '../data/US04/US04_five.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)
            
    #
    # US05
    #

    def test_US05_one(self):
        # valid family -- should pass
        try:
            filename = '../data/US05/US05_one.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_US05_two(self):
        # death before marriage -- should fail
        try:
            filename = '../data/US05/US05_two.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_US05_three(self):
        # death on marriage day -- should pass
        try:
            filename = '../data/US05/US05_three.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_US05_four(self):
        # death one month after marriage date -- should pass
        try:
            filename = '../data/US05/US05_four.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_US05_five(self):
        # death one month before marriage date -- should fail
        try:
            filename = '../data/US05/US05_five.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)
    
    #
    # US06
    #

    def test_US06_one(self):
        # valid family -- should pass
        try:
            filename = '../data/US06/US06_one.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_US06_two(self):
        # death before divorce -- should fail
        try:
            filename = '../data/US06/US06_two.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_US06_three(self):
        # death on divorce day -- should pass
        try:
            filename = '../data/US06/US06_three.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_US06_four(self):
        # death one month after divorce date -- should pass
        try:
            filename = '../data/US06/US06_four.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_US06_five(self):
        # death one month before divorce date -- should fail
        try:
            filename = '../data/US06/US06_five.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    #
    # US07
    #

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

    #
    # US08
    #

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