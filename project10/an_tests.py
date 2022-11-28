import unittest
import sys
sys.path.insert(1, '../')
from main import Family

class Test(unittest.TestCase):

    def test_US27(self):
        filename = '../data/US25/US25.ged'
        fam = Family(filename)
        fam.create_family(filename)
        self.assertTrue(fam.exceptions != [])
    
    def test_US34(self):
        filename = '../data/US34/US34.ged'
        fam = Family(filename)
        fam.create_family(filename)
        age_dff = fam.list_large_age_dff()
        self.assertTrue(age_dff != [])

if __name__ == '__main__':
    unittest.main()