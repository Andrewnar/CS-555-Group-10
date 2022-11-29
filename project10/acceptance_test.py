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
        print('US27:')
        print(family.list_include_ages())
        print('\nUS28:')
        print(family.order_siblings())
        print('\nUS29:')
        print(family.list_deceased())
        print('\nUS30:')
        print(family.list_living_married())
        print('\nUS31:')
        print(family.list_living_single())
        print('\nUS32:')
        print(family.list_mult_births())
        print('\nUS34:')
        print(family.list_large_age_dff())
