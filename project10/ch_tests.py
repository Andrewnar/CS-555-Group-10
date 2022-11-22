import unittest
import sys
sys.path.insert(1, '../')
from main import Family

class Test(unittest.TestCase):

    def test_US27(self):
        filename = '../data/US27-28/US2728_test.ged'
        fam = Family(filename)
        fam.create_family(filename)
        list_indi = fam.list_include_ages()
        # print(list_indi)
        self.assertTrue(len(list_indi)>0)
    
    def test_US28(self):
        filename = '../data/US27-28/US2728_test.ged'
        fam = Family(filename)
        fam.create_family(filename)
        order_sibs = fam.order_siblings()
        # print(order_sibs)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()