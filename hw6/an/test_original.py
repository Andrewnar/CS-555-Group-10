import unittest
import sys
sys.path.insert(1, '../')
from original import Family #change to original.py to test non_smelly code


class Test(unittest.TestCase):
    def test_I5(self):
        try:
            filename = 'data/testfamily.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.people["I5"][3] == 24)
        except Exception:
            self.assertTrue(False)
    
    def test_family_children_size(self):
        try:
            filename = 'data/testfamily.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(len(family.family["F11"][6]) == 17)
        except Exception:
            self.assertTrue(False)

    def test_married(self):
        try:
            filename = 'data/testfamily.ged'
            family = Family(filename)
            family.create_family(filename)
            self.assertTrue(family.family["F3"][2] == "I8" and family.family["F3"][4] == "I9")
        except Exception:
            self.assertTrue(False)

    def test_inorder(self):
        try:
            filename = 'data/testfamily.ged'
            family = Family(filename)
            family.create_family(filename)
            keys = list(family.people.keys())
            for i in range(len(keys)):
                keys[i] = int(keys[i][1:])
            
            self.assertTrue(keys != sorted(keys)) # will show that its out of order
        except Exception:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()