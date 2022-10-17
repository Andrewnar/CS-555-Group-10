import sys
sys.path.insert(1, '../')
from main import Family
import sys

if __name__ == '__main__':
    filename = '../data/testfamily.ged'
    family = Family(filename)
    family.create_family(filename)
    with open('testoutput.txt', 'w') as sys.stdout:
        print(family)