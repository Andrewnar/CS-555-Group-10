from project4 import Family

if __name__ == '__main__':
    filename = '../data/testfamily.ged'
    family = Family(filename)
    family.create_family(filename)
    print(family)