import unittest
import sys
sys.path.insert(1, '../')
from main import Family

class Test(unittest.TestCase):

    # def test_US19_US20_one(self):
    #     filename = "../data/US19/US19_good.ged"
    #     fam = Family(filename)
    #     fam.create_family(filename)
        
    #     self.assertTrue(fam.exceptions == [])

    # def test_US19_one(self):
    #     filename = "../data/US19/US19_bad.ged"
    #     fam = Family(filename)
    #     fam.create_family(filename)
    #     # print(fam)
    #     self.assertTrue(fam.exceptions != [])

    # aunt and uncle are married
    def test_US20_one(self):
        filename = "../data/US20/US20_bad.ged"
        fam = Family(filename)
        fam.create_family(filename)
        # print(fam)
        print(fam.exceptions)
        self.assertTrue(fam.exceptions != [])

if __name__ == '__main__':
    unittest.main()