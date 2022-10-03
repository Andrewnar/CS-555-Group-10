import sys
import pprint
import collections
from datetime import datetime
from datetime import timedelta
from datetime import date
from collections import OrderedDict
from prettytable import PrettyTable
from dateutil.relativedelta import relativedelta

# 
printToFile = False
if printToFile:
    f = open('project3output.txt','w')
    sys.stdout = f  

def calc_age(birthdate):
    # Calculate age from datetime obj
    # https://www.codingem.com/how-to-calculate-age-in-python/
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

class Family:

    def __init__(self, filename):
        self.people = {} # { ID : [Name, Gender, Birthday, Age, Alive, Death, [Child], [Spouse]] }
        self.family = {} # { Family_ID : [Married, Divorced, Husband_ID, Husband_Name, Wife_ID, Wife_Name, [Children]] }
        self.file = filename


    def __str__(self):
        # To sort dictionary by key we can also make it an order dict and apply
        # people = collections.OrderedDict(sorted(self.people.items()))
        # family = collections.OrderedDict(sorted(self.family.items()))

        t = PrettyTable(['ID', 'Name', 'Gender', "Birthday", 'Age', 'Alive', 'Death', 'Child', 'Spouse'])
        for key, val in self.people.items():
            t.add_row([key, val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7]])
        print(t)

        f = PrettyTable(['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
        for key, val in self.family.items():
            f.add_row([key, val[0], val[1], val[2], val[3], val[4], val[5], val[6]])
        print(f)
        return ""
    

    def gen_rest_args(self):
        # Will update spouses and children for individuals
        people = self.people 
        family = self.family
        for family_id, args in family.items():
            if args[1] == "N/A":
                # Marriage without divorce... curr spouse!
                people[args[2]][7] = args[4]
                people[args[4]][7] = args[2]

            # Have to update children for each individual regardless of divorce
            dad_chil = [] if people[args[2]][6] == "N/A" else people[args[2]][6]
            mom_chil = [] if people[args[4]][6] == "N/A" else people[args[4]][6]

            children = [] if args[6] == "N/A" else args[6]

            # Set children
            people[args[2]][6] = dad_chil + children
            people[args[4]][6] = mom_chil + children

        self.people = people
        self.family = family


    def check_constraints(self):
        # This function will check the constraints defined by the user stories

        # USO3 Birth before death - ch
        for (id, person) in self.people.items():
            # if there is a death date
            if person[5] != 'N/A':
                # get birth and death dates of each person
                birthday = datetime.strptime(person[2], '%d %b %Y').date()
                death_date = datetime.strptime(person[5], '%d %b %Y').date() 
                if (birthday-death_date).days > 0: # check if birthday is after the death day
                    raise Exception(f"Error: Person [{id}] cannot have a death date that precedes a birth date")

        # US04 Marriage before divorce - ch
        for (id, info) in self.family.items():        
            # if there is no marriage dates in the family
            if info[0] == 'N/A':
                raise Exception(f"Error: Family [{id}] does not have a marriage date")

            # if there is a divorce date
            if info[1] != 'N/A':
                # get the dates of the marriage and divorce
                marriage_date = datetime.strptime(info[0], '%d %b %Y').date()
                divorce_date = datetime.strptime(info[1], '%d %b %Y').date()
                # check if marriage comes after the divorce date
                if((marriage_date - divorce_date).days > 0 ):
                    raise Exception(f"Error: Family [{id}] cannot get divorced before marriage")
                # check if the divorce comes 30 days after the marriage date
                if ((marriage_date - divorce_date).days > -30) : # check if the marriage date comes after the divorce date
                        raise Exception(f"Error: Family [{id}] can only get divorced 30 days after marriage")

        # US05 Marriage before death - rc
        for (id, info) in self.family.items():
            # in info:
            # married date = info[0]
            # husband id = info[2]
            # wife id = info[4]
            if info[0] == 'N/A':
                raise Exception(f"Error: Family [{id}] does not have a marriage date")

            marriage_date = datetime.strptime(info[0], '%d %b %Y').date()
            husband = self.people.get(info[2])
            wife = self.people.get(info[4])
            
            if husband[5] != 'N/A': #check husband
                #husband is dead
                death_date = datetime.strptime(husband[5], '%d %b %Y').date()
                if death_date < marriage_date:
                    raise Exception(f"Error: Person [{info[2]}] can not be married after death.")
    
            if wife[5] != 'N/A': #check wife
                #wife is dead
                death_date = datetime.strptime(wife[5], '%d %b %Y').date()
                if death_date < marriage_date:
                    raise Exception(f"Error: Person [{info[2]}] can not be married after death.")
        
        # US06 Divorce before death - rc
        for (id, info) in self.family.items():
            # in info:
            # divorce date = info[1]
            # husband id = info[2]
            # wife id = info[4]
            if info[1] != 'N/A': #look for a divorce
                divorce_date = datetime.strptime(info[1], '%d %b %Y').date()
                husband = self.people.get(info[2])
                wife = self.people.get(info[4])

                if husband[5] != 'N/A': #check husband
                    #husband is dead
                    death_date = datetime.strptime(husband[5], '%d %b %Y').date()
                    if death_date < divorce_date:
                        raise Exception(f"Error: Person [{info[2]}] can not get a divorce after death.")
    
                if wife[5] != 'N/A': #check wife
                    #wife is dead
                    death_date = datetime.strptime(wife[5], '%d %b %Y').date()
                    if death_date < divorce_date:
                        raise Exception(f"Error: Person [{info[2]}] can not get a divorce after death.")

        # US07 Less than 150 years old
        for (id, info) in self.people.items(): # loop through all persons
            if not info[4]: # if the person is dead, check our death constraints
                # get date objects for birth and death date strings
                death_date = datetime.strptime(info[5], '%d %b %Y').date()
                birth_date = datetime.strptime(info[2], '%d %b %Y').date()

                # Check if death date is less than 150 years after birth date, error if not
                if death_date - birth_date >= timedelta(days=54750):
                    raise Exception(f"Person [{id}]'s death date must be less than 150 years after birth date")
            else: # if the person is alive, check our living constraints
                today = date.today() # get today's date
                birth_date = datetime.strptime(info[2], '%d %b %Y').date() # get birth date

                if today - birth_date >= timedelta(days=54750):
                    raise Exception(f"Person [{id}] must be less than 150 years old")
        
        # US08 Birth before marriage of parents
        for (id, fam_info) in self.family.items(): # loop through all families
            # get marriage date as a date object
            marriage_date = datetime.strptime(fam_info[0], '%d %b %Y').date()
            
            divorced = not fam_info[1] == 'N/A'
            divorced_date = None
            constraint_date = None
            if divorced:
                # get divorce date
                divorce_date = datetime.strptime(fam_info[1], '%d %b %Y').date()
                
                # get the constraint date
                constraint_date = divorce_date + relativedelta(months=9)

            # loop through all children if they exist
            if not fam_info[6] == 'N/A':
                for child in fam_info[6]:
                    birth_date = datetime.strptime(self.people[child][2], '%d %b %Y').date()

                    # check if birthdate is > marriage date, error if not
                    if not birth_date > marriage_date:
                        raise Exception(f"Child [{child}] should be born after parents' marriage")
                    
                    # if the family has been divorced, check the the divorce constraints
                    if divorced:
                        # if the child's birth date is greater than 9 months after the divorce date, error
                        if birth_date > constraint_date:
                            raise Exception(f"Child [{child}]'s birth date must be no more than 9 months after parents' divorce")


    def create_family(self, filename):
        people = self.people 
        family = self.family
        filename = self.file

        # Valid Tags { Tag : Level }
        validDict = { "INDI": 0, "NAME": 1,"SEX": 1,"BIRT":1,"DEAT":1,"FAMC":1,"FAMS":1,"FAM":0,
                    "MARR":1,"HUSB":1,"WIFE":1,"CHIL":1,"DIV":1,"DATE":2,"HEAD":0,"TRLR":0,"NOTE":0 } 

        with open(filename) as file:
            curr_person = None
            curr_family = None
            prev_tag = None

            for line in file:
                line = line.replace('@', "")
                line = line.rstrip().split()


                # handles when arguemnt and tag are swapped bc of exception listed in proejct 2
                if len(line) > 2 and (line[2] == 'INDI' or line[2] == 'FAM'):
                    line[1], line[2] = line[2], line[1]

                # if tag + level isn't valid, continue
                level, tag = int(line[0]), line[1] 
                if tag not in validDict or level != validDict[tag]:
                    continue
                
                # set rest of arguments to be a str
                args = ' '.join(line[2:])

                # BEGIN FILLING OUT PERSONS/FAMILIES

                if level == 0: # Indicates a new record...
                    if tag == "INDI":
                        # New Person
                        curr_person = args
                        people[curr_person] = ["N/A"] * 8
                        continue 

                    if tag == "FAM":
                        # New Family
                        curr_family = args
                        family[curr_family] = ["N/A"] * 7
                        continue


                # reference = ["NAME", "SEX", "BIRT", "AGE", "DEATH","CHILD","SPOUSE"]
                if tag == "NAME":
                    people[curr_person][0] = args
                if tag == "SEX":
                    people[curr_person][1] = args

                if tag in ["BIRT", "DEAT", "MARR", "DIV"]: # need to save tag so we know where to store date
                    prevTag = tag
                    continue
                
                if tag == "DATE": 
                    if prevTag in ["BIRT", "DEAT"]:
                        # part of person
                        if prevTag == "BIRT": # have to fill age
                            months = ["", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
                            age = calc_age(date(int(line[4]), months.index(line[3]), int(line[2])))
                            people[curr_person][2] = args
                            people[curr_person][3] = age
                            people[curr_person][4] = True

                        if prevTag == "DEAT":
                            # TODO update age so it calculates based on death not simply birth
                            people[curr_person][4] = False
                            people[curr_person][5] = args 
                    else:
                        # part of family
                        # TODO create flags for if prevTag is MARR or DIV and fill out for each
                        if prevTag == "MARR":
                            family[curr_family][0] = args
                        if prevTag == "DIV":
                            family[curr_family][1] = args

                        

                # TODO Update Family Collection
                # { Family_ID : [Married, Divorced, Husband_ID, Husband_Name, Wife_ID, Wife_Name, [Children]] }

                if tag == "HUSB" or tag == "WIFE":
                    #TODO individual_id of husband of family...
                    temp_id = 2
                    temp_name = 3
                    if tag == "WIFE":
                        temp_id = 4
                        temp_name = 5
                    family[curr_family][temp_id] = args
                    family[curr_family][temp_name] = people[args][0]

                if tag == "CHIL":
                    #TODO Indiviudal_id of CHIL of family
                    children = family[curr_family][6]
                    if children == "N/A":
                        children = []
                    children += [args]

                    family[curr_family][6] = children 
                    
                if tag == "FAMC" or tag == "FAMS":
                    # tags will be handled at end --> self.gen_rest_args()
                    # this will loop through family and set children/spouses for individuals
                    pass
            
        self.people = people
        self.family = family
        self.gen_rest_args()
        self.check_constraints()

  
if __name__ == '__main__':
    filename = "../data/RyanClarkTestFamily.ged"
    andrew_fam = Family(filename)
    andrew_fam.create_family(filename)
    print(andrew_fam)
