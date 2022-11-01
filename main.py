from re import M
import sys
import time
import pprint
import collections
from datetime import datetime
from datetime import timedelta
from datetime import date
from collections import defaultdict
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
        self.exceptions = []


    def __str__(self):
        # To sort dictionary by key we can also make it an order dict and apply
        # people = collections.OrderedDict(sorted(self.people.items()))
        # family = collections.OrderedDict(sorted(self.family.items()))

        self.sortDict()

        t = PrettyTable(['ID', 'Name', 'Gender', "Birthday", 'Age', 'Alive', 'Death', 'Child', 'Spouse'])
        for key, val in self.people.items():
            t.add_row([key, val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7]])
        print(t)

        f = PrettyTable(['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
        for key, val in self.family.items():
            f.add_row([key, val[0], val[1], val[2], val[3], val[4], val[5], val[6]])
        print(f)

        # exceptions = self.exceptions
        # exceptions = set(exceptions)
        # self.exceptions = exceptions

        for excep in self.exceptions:
            print(excep)
        return ""

    def sortDict(self):
        temp_peeps = {}
        temp_fam = {}

        for k, v in self.people.items():
            k = int(k[1:]) # removes 'I'
            temp_peeps[k] = v

        for k, v in self.family.items():
            k = int(k[1:]) # removes 'F'
            temp_fam[k] = v

        self.people = collections.OrderedDict(sorted(temp_peeps.items()))
        self.family = collections.OrderedDict(sorted(temp_fam.items()))

        temp_peeps, temp_fam = {}, {}

        for k, v in self.people.items():
            k = "I" + str(k) # adds 'I'
            temp_peeps[k] = v

        for k, v in self.family.items():
            k = "F" + str(k) # adds 'F'
            temp_fam[k] = v

        self.people, self.family = temp_peeps, temp_fam
    

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

    # converts a date string in the form 00 MON YEAR to a date object
    def convert_to_date(self, string):
        return datetime.strptime(string, '%d %b %Y').date()

    # returns none if there is no divorce date, otherwise returns the date object of the divorce date
    def get_divorce_date(self, fam_info):
        if fam_info[1] == 'N/A':
            return None
        else:
            return self.convert_to_date(fam_info[1])

    def check_constraints(self):
        # This function will check the constraints defined by the user stories

        ##############
        ## SPRINT 1 ##
        ##############

        # US01 Dates shouldn't be after current date - an
        for (id, person) in self.people.items():
            today = date.today()
            birthday = datetime.strptime(person[2], '%d %b %Y').date()
            if person[5] != 'N/A':
                death_date = datetime.strptime(person[5], '%d %b %Y').date()
                if death_date > today:
                    self.exceptions += [(f"ERROR: INDIVIDUAL: US01: [{id}]: has death_date {death_date} that occurs in the future")]
            # print(birthday, today, birthday > today) 
            if birthday > today:
                self.exceptions += [(f"ERROR: INDIVIDUAL: US01: [{id}]: has birthday {birthday} that occurs in the future")]

        for (id, family) in self.family.items():
            today = date.today()
            marriage = datetime.strptime(family[0], '%d %b %Y').date()
            if family[1] != 'N/A':
                divorce = datetime.strptime(family[1], '%d %b %Y').date()
                if divorce > today:
                    self.exceptions += [(f"ERROR: FAMILY: US01: [{id}]: has divorce {divorce} that occurs in the future")]
            # print(birthday, today, birthday > today) 
            if marriage > today:
                self.exceptions += [(f"ERROR: FAMILY: US01: [{id}]: has marriage {marriage} that occurs in the future")]

            # US02 Birth should occur before marriage of individual
            husband, wife = family[2], family[4]
            husband_birth, wife_birth = datetime.strptime(self.people[husband][2], '%d %b %Y').date(), datetime.strptime(self.people[wife][2], '%d %b %Y').date()  

            if marriage < husband_birth :
                self.exceptions += [(f"ERROR: FAMILY: US02: [{id}]: Individual [{family[2]}] has marriage {marriage} that occurs before birthdate {husband_birth}")]
            if marriage < wife_birth :
                self.exceptions += [(f"ERROR: FAMILY: US02: [{id}]: Individual [{family[4]}] has marriage {marriage} that occurs before birthdate {wife_birth}")]


        

        # USO3 Birth before death - ch
        for (id, person) in self.people.items():
            # if there is a death date
            if person[5] != 'N/A':
                # get birth and death dates of each person
                birthday = datetime.strptime(person[2], '%d %b %Y').date()
                death_date = datetime.strptime(person[5], '%d %b %Y').date() 
                if (birthday-death_date).days > 0: # check if birthday is after the death day
                   self.exceptions += [(f"ERROR: INDIVIDUAL: US03: [{id}] cannot have a death date that precedes a birth date")]

        # US04 Marriage before divorce - ch
        for (id, info) in self.family.items():        
            # if there is no marriage dates in the family
            if info[0] == 'N/A':
                self.exceptions += [(f"ERROR: FAMILY: US04:  [{id}] does not have a marriage date")]

            # if there is a divorce date
            if info[1] != 'N/A':
                # get the dates of the marriage and divorce
                marriage_date = datetime.strptime(info[0], '%d %b %Y').date()
                divorce_date = datetime.strptime(info[1], '%d %b %Y').date()
                # check if marriage comes after the divorce date
                if((marriage_date - divorce_date).days > 0 ):
                    self.exceptions += [(f"ERROR: FAMILY: US04: [{id}] cannot get divorced before marriage")]
                # check if the divorce comes 30 days after the marriage date
                if ((marriage_date - divorce_date).days > -30) : # check if the marriage date comes after the divorce date
                        self.exceptions += [(f"ERROR: FAMILY: US04: [{id}] can only get divorced 30 days after marriage")]

        # US05 Marriage before death - rc
        for (id, info) in self.family.items():
            # in info:
            # married date = info[0]
            # husband id = info[2]
            # wife id = info[4]
            if info[0] == 'N/A':
                self.exceptions += [(f"ERROR: FAMILY: US05: [{id}] does not have a marriage date")]

            marriage_date = datetime.strptime(info[0], '%d %b %Y').date()
            husband = self.people.get(info[2])
            wife = self.people.get(info[4])
            
            if husband[5] != 'N/A': #check husband
                #husband is dead
                death_date = datetime.strptime(husband[5], '%d %b %Y').date()
                if death_date < marriage_date:
                    self.exceptions += [(f"ERROR: INDIVIDUAL: US05: [{info[2]}] can not be married after death.")]
    
            if wife[5] != 'N/A': #check wife
                #wife is dead
                death_date = datetime.strptime(wife[5], '%d %b %Y').date()
                if death_date < marriage_date:
                    self.exceptions += [(f"ERROR: INDIVIDUAL: US05: [{info[2]}] can not be married after death.")]
        
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
                        self.exceptions += [(f"ERROR: INDIVIDUAL: US06: [{info[2]}] can not get a divorce after death.")]
    
                if wife[5] != 'N/A': #check wife
                    #wife is dead
                    death_date = datetime.strptime(wife[5], '%d %b %Y').date()
                    if death_date < divorce_date:
                        self.exceptions += [(f"ERROR: INDIVIDUAL: US06: [{info[2]}] can not get a divorce after death.")]

        # US07 Less than 150 years old
        for (id, info) in self.people.items(): # loop through all persons
            if not info[4]: # if the person is dead, check our death constraints
                # get date objects for birth and death date strings
                death_date = self.convert_to_date(info[5])
                birth_date = self.convert_to_date(info[2])

                # Check if death date is less than 150 years after birth date, error if not
                if death_date - birth_date >= timedelta(days=54750):
                    self.exceptions += [(f"ERROR: INDIVIDUAL: US07: [{id}]'s death date must be less than 150 years after birth date")]
            else: # if the person is alive, check our living constraints
                today = date.today() # get today's date
                birth_date = self.convert_to_date(info[2]) # get birth date

                if today - birth_date >= timedelta(days=54750):
                    self.exceptions += [(f"ERROR: INDIVIDUAL: US07: [{id}] must be less than 150 years old")]
        
        # US08 Birth before marriage of parents
        for (id, fam_info) in self.family.items(): # loop through all families
            # get marriage date as a date object
            marriage_date = self.convert_to_date(fam_info[0])
            
            # get properly formatted divorce date if it exists
            divorce_date = self.get_divorce_date(fam_info)
            if not divorce_date == None:
                # get the constraint date
                constraint_date = divorce_date + relativedelta(months=9)

            # loop through all children if they exist
            if not fam_info[6] == 'N/A':
                for child in fam_info[6]:
                    birth_date = self.convert_to_date(self.people[child][2])

                    # check if birthdate is > marriage date, error if not
                    if not birth_date > marriage_date:
                        self.exceptions += [(f"ERROR: INDIVIDUAL: US08: Child [{child}] should be born after parents' marriage")]
                    
                    # if the family has been divorced, check the the divorce constraints
                    if not divorce_date == None:
                        # if the child's birth date is greater than 9 months after the divorce date, error
                        if birth_date > constraint_date:
                            self.exceptions += [(f"ERROR: INDIVIDUAL: US08: Child [{child}]'s birth date must be no more than 9 months after parents' divorce")]

        ##############
        ## SPRINT 2 ##
        ##############

        # US09 Child born before death of parents
        # US10 Parents must be 14 years of age before marriage
        temp_exceptions = []
        for(id, family) in self.family.items():
            fatherID, motherID = family[2], family[4]
            if family[6] != 'N/A': # children
                for child in family[6]:
                    child_info = self.people[child]
                    child_bday = datetime.strptime(child_info[2], '%d %b %Y').date()
                    if not self.people[fatherID][4]: # father dead
                        temp_bday_child = child_bday + relativedelta(months=9)
                        if(temp_bday_child > datetime.strptime(self.people[fatherID][5], '%d %b %Y').date()):
                            self.exceptions += [(f"ERROR: INDIVIDUAL: US09: Child [{child}] should be born [{child_bday}] atleast 9 months before father's death [{self.people[fatherID][5]}]")]

                    if not self.people[motherID][4]: # mom dead
                        if child_bday > datetime.strptime(self.people[motherID][5], '%d %b %Y').date():
                            self.exceptions += [(f"ERROR: INDIVIDUAL: US09: Child [{child}] should be born [{child_bday}] before mother's death [{self.people[motherID][5]}]")]

            married_date, dad_age, mom_age = datetime.strptime(family[0], '%d %b %Y').date(), datetime.strptime(self.people[fatherID][2], '%d %b %Y').date(), datetime.strptime(self.people[motherID][2], '%d %b %Y').date()
            dad_marry_age, mom_marry_age = dad_age + relativedelta(months=168), mom_age + relativedelta(months=168)
            # print(dad_marry_age > married_date, mom_marry_age)
            if dad_marry_age > married_date:
                 temp_exceptions += [(f"ERROR: INDIVIDUAL: US10: Individual [{fatherID}] should be 14 years older then marry date [{married_date}]")]
            if mom_marry_age > married_date:
                 temp_exceptions += [(f"ERROR: INDIVIDUAL: US10: Individual [{motherID}] should be 14 years older then marry date [{married_date}]")]
        self.exceptions += temp_exceptions
        # US11 No Bigamy
        # { Family_ID : [Married, Divorced, Husband_ID, Husband_Name, Wife_ID, Wife_Name, [Children]] }
        bigamy_dict = defaultdict(list) # Individual_ID : [(start_marriage, end_marriage)]
        for(id, family) in self.family.items():
            married_date = datetime.strptime(family[0], '%d %b %Y').date()
            divorced_date = date.today() if family[1] == "N/A" else datetime.strptime(family[1], '%d %b %Y').date()
            bigamy_dict[family[2]] += [(married_date,divorced_date)]
            bigamy_dict[family[4]] += [(married_date,divorced_date)]
        today = date.today()
        
        # key : value --> id: [(start,end), (start,end)]
        for id, date_range in bigamy_dict.items():
            # date_range = [(start, end), (start, end)]
            max_end = None
            date_range = sorted(date_range)
            for start, end in date_range:
                if max_end == None:
                    max_end = end
                else:
                    if start < max_end:
                        self.exceptions += [(f"ERROR: INDIVIDUAL: US11: Individual [{id}] commited bigamy!")]
                    if max_end < end:
                        max_end == end
                # change max_end
                # Bob --> (1992, 2001), (2002, 2004), (2003, 2009)
                # Mary --> (1992, 2001), (2005, 2008), ()


        # US12 Parents not too old
        # helper to refactor and make getting parents ages easier
        def getParentsAge(family):
            mother = family[4]
            father = family[2]
            dad_age = datetime.strptime(self.people[father][2], '%d %b %Y').date()
            mom_age = datetime.strptime(self.people[mother][2], '%d %b %Y').date()
            return [dad_age, mom_age]
        
        def calcAge(dad_age, mom_age, dad_increment, mom_increment):
            return [dad_age+dad_increment, mom_age+mom_increment]
        # loop through families
        for(id, family) in self.family.items():
            # mother +60, father +80
            # old code
            # mother = family[4]
            # father = family[2]
            # dad_age = datetime.strptime(self.people[father][2], '%d %b %Y').date()
            # mom_age = datetime.strptime(self.people[mother][2], '%d %b %Y').date()
            # dad_age = parents_age[0]
            # mom_age = parents_age[1]
            # dad_age += relativedelta(months=960)
            # mom_age += relativedelta(months=720)

            # refactored code 1. find parents age in separate function 2. calculate increments in age for parents
            # get +80 father age, +60 mother age
            parents_age = getParentsAge(family)
            newAges = calcAge(parents_age[0], parents_age[1], relativedelta(months=960), relativedelta(months=720))
            children = family[6]
            child_age = 0
            for child in children:
                if child == 'N': break
                child_age = datetime.strptime(self.people[child][2], '%d %b %Y').date()
                if newAges[0] < child_age or newAges[1] < child_age:
                    self.exceptions += [(f"ERROR: INDIVIDUAL: US12: Child [{child}]'s parents are too old!")]

        # US13 Siblings spacing
        for (id, family) in self.family.items():
            children = family[6]
            if (children != 'N/A'):
                birthdays = []
                for child in children:
                    child_data = self.people.get(child)
                    birthdays += [child_data[2]]
                two_days = timedelta(days=2)
                eight_months = timedelta(days=243)
                for i in range(0,len(birthdays)):
                    for j in range(i + 1,len(birthdays)):
                        time_one = datetime.strptime(birthdays[i], '%d %b %Y').date()
                        time_two = datetime.strptime(birthdays[j], '%d %b %Y').date()
                        if time_one - time_two > two_days and time_one - time_two < eight_months:
                                self.exceptions += [(f"ERROR: FAMILY: US13: Family [{id}]: Birth dates of siblings should be more than 8 months apart or less than 2 days apart")]
                        if time_two - time_one > two_days and time_two - time_one < eight_months:
                                self.exceptions += [(f"ERROR: FAMILY: US13: Family [{id}]: Birth dates of siblings should be more than 8 months apart or less than 2 days apart")]

        # US14 Multiple Births <= 5
        for (id, family) in self.family.items():
            children = family[6] #children from one family
            if (children != 'N/A'):
                frequencies = {} #create frequency dict
                for child in children:
                    child_data = self.people.get(child) 
                    #if child is in dictionary, increment, otherwise init to 1
                    if child_data[2] in frequencies:
                        frequencies[child_data[2]] += 1
                    else:
                        frequencies[child_data[2]] = 1
                for (repeat_date, frequency) in frequencies.items():
                    if (frequency > 5): #check if any frequency is up to 5
                        self.exceptions += [(f"ERROR: FAMILY: US14: [{id}] No more than five siblings should be born at the same time. {frequency} were born on {repeat_date}")]

        # US15 Fewer than 15 siblings
        for id, family in self.family.items():
            children = family[6] # get the children from the family
            if children != 'N/A':
                if len(children) > 15: # check constraint
                    self.exceptions += [f"ERROR: FAMILY: US15: [{id}] There should be fewer than 15 siblings in a family. There are [{len(children)-1}] siblings in this family"]

        # US16 Male last names
        for id, family in self.family.items():
            last_name = family[3].split(' ', 1)[1] # get last name of husband
            children = family[6] # get the children from the family
            if children != 'N/A':
                for child_id in children:
                    child = self.people[child_id]
                    if child[1] == 'M':
                        child_last = child[0].split(' ', 1)[1] # get last name of male child
                        if last_name != child_last:
                            self.exceptions += [f"ERROR: INDIVIDUAL: US16: [{id}] All male members of a family should have the same last name. Child [{child_id}] does not have the same last name as the father [{child_last}]"]

        ##############
        ## SPRINT 3 ##
        ##############
        
        # US17 No marriages to descendants
        for id, family in self.family.items():
            mom, dad, children = family[2], family[4], family[6]
            mom_descendents = []
            dad_descendents = []

            def recursiveChildren(id):
                id_children = self.people[id][6]
                if id_children == "N/A":
                    return [id]
                if id in id_children:
                    return id_children
                res = []
                # print(id, id_children)
                for child in id_children:
                    res += recursiveChildren(child)
                
                return res
            mom_descendents = recursiveChildren(mom)
            dad_descendents = recursiveChildren(dad)
            if dad in mom_descendents:
                self.exceptions += [f"ERROR: FAMILY: US17: [{mom}] is married to his descendent [{dad}]"]
            if mom in dad_descendents:
                self.exceptions += [f"ERROR: FAMILY: US17: [{dad}] is married to her descendent [{mom}]"]

        # US18 Siblings should not marry
        siblingsDict = {}
        for id, people in self.people.items():
            def getSiblingsOfID(id):
                siblings = []
                for famid, family in self.family.items():
                    if family[6] == "N/A":
                        pass
                    if id in family[6]:
                        siblings += family[6]
                return siblings
            siblings = getSiblingsOfID(id)
            siblingsDict[id] = siblings
        
        for id, family in self.family.items():
            dad, mom = family[2], family[4]
            # print(dad, siblingsDict[dad], mom, siblingsDict[mom])
            if mom in siblingsDict[dad] or dad in siblingsDict[mom]:
                self.exceptions += [f"ERROR: FAMILY: US18: [{mom}] is married to her sibling [{dad}]"]

        # US19 First cousins should not marry
        '''
        for each person
            get their children and siblings children []
                check if children in married to siblings children
            
        '''

        def getFstChildren(id):
            children = self.people[id][6]
            if children == "N/A":
                children = []
            return children
        
        def getMultipleChildren(id_arr):
            children = []
            for ids in id_arr:
                childs = getFstChildren(ids)
                children += childs
            return children

        for id, family in self.family.items():
            dad, mom = family[2], family[4]
            dad_siblings, mom_siblings = getSiblingsOfID(dad), getSiblingsOfID(mom)

            dad_children, mom_children = getFstChildren(dad), getFstChildren(mom)
            dad_siblings_children, mom_siblings_children = getMultipleChildren(dad_siblings), getMultipleChildren(mom_siblings)
            fam_children, cousins = dad_children+mom_children, dad_siblings_children+mom_siblings_children

            for id2, family2 in self.family.items():
                dad2, mom2 = family2[2], family2[4]
                # print(dad2, mom2, fam_children, cousins)
                if dad2 in fam_children:
                    if mom2 in cousins:
                        self.exceptions += [f"ERROR: FAMILY: US19: [{mom2}] is married to her 1st cousin [{dad2}]"]
                elif dad2 in cousins:
                    if mom2 in fam_children:
                        self.exceptions += [f"ERROR: FAMILY: US19: [{mom2}] is married to her 1st cousin [{dad2}]"]















        # for id, family in self.family.items():    
        #     mom, dad, children = family[2], family[4], family[6]
        #     momSiblings = siblingsDict[mom]
        #     dadSiblings = siblingsDict[dad]   
        #     momSideCousins = []
        #     dadSideCousins = []
        #     # get all of mom's sides cousins
        #     for momSib in momSiblings:
        #         momSibChildren = getSiblingsOfID(momSib)
        #         momSideCousins += momSibChildren
        #     # get all of dad's sides cousins
        #     for dadSib in dadSiblings:
        #         dadSibChildren = getSiblingsOfID(dadSib)
        #         dadSideCousins += dadSibChildren
        #     if momCuz in momSideCousins:
        #         self.exceptions += [f"ERROR: FAMILY: US20: Aunts and Uncles cannot marry"]
        #     mom_descendents = recursiveChildren(mom)
        #     dad_descendents = recursiveChildren(dad)

        # US20 Aunts and uncles a.k.a mom's siblings cant marry dad's siblings
        # create tuples of all married couples, compare to see if the mom and dad in tuples are in related families?
        cantMarry = []
        for id, family in self.family.items():
            # print(family)
            if family[0] != 'N/A':
                dad, mom = family[2], family[4]
                for momSib in siblingsDict[mom]:
                    if momSib in cantMarry:
                        exceptions = self.exceptions
                        exception_temp = f"ERROR: FAMILY: US20: [{mom}] is married to [{dad}]"
                        print(type(exception_temp), type(exceptions[0]))
                        if exception_temp not in exceptions:
                            self.exceptions += [f"ERROR: FAMILY: US20 : [{mom}] is married to [{dad}]"]
                            break
                    cantMarry.append(momSib)
                for dadSib in siblingsDict[dad]:
                    if dadSib in cantMarry:
                        exceptions = self.exceptions
                        exception_temp = f"ERROR: FAMILY: US20: [{mom}] is married to [{dad}]"
                        if exception_temp not in exceptions:
                            self.exceptions += [f"ERROR: FAMILY: US20 : [{mom}] is married to [{dad}]"]
                            break
                    cantMarry.append(dadSib)

        # US21 Correct gender for role
        # Husband in family should be male and wife in family should be female
        for id, family in self.family.items():
            husband = self.people.get(family[2])
            wife = self.people.get(family[4])
            if husband[1] != 'M':
                self.exceptions += [f"ERROR: FAMILY: US21: [{id}] Husband must be male"]
            if wife[1] != 'F':
                self.exceptions += [f"ERROR: FAMILY: US21: [{id}] Wife must be female"]

        # US22 Unique IDs
        # All individual IDs should be unique and lal family IDs should be unique
        # check for duplicate family ids
        family_ids = []
        for id, family in self.family.items():
            if id in family_ids:
                self.exceptions += [f"ERROR: FAMILY: US22: [{id}] Cannot have duplicate family ids"]
            else:
                family_ids += [id]
        # check for duplicate person ids
        person_ids = []
        for id, info in self.people.items():
            if id in person_ids:
                self.exceptions += [f"ERROR: INDIVIDUAL: US22: [{id}] Cannot have duplicate person ids"]
            else:
                person_ids += [id]

        # US23 Unique name and birth date
        name_bday = {} # keep track of name,bday pairings we've seen
        for id, info in self.people.items():
            bday = info[2] # get birthday
            name = info[0] # get name
            if bday in name_bday: # check if we've seen this birthday before
                if name in name_bday[bday]: # check if there is already an occurance of this name on this birthday, error if so
                    self.exceptions += [f"ERROR: INDIVIDUAL: US23: [{id}] Cannot have multiple people with the same name and birthday"]
                else: # add this name to this birthday if not
                    name_bday[bday].append(name)
            else: # add this birthday with the name to the dictionary
                name_bday[bday] = [name]
        
        # US24 Unique families by spouses
        spouse_date = {} # keep track of spouse,marriage date pairings we've seen
        for id, info in self.family.items():
            marriage_date = info[0] # get marriage date
            husband_name = info[3] # get husband's name
            wife_name = info[5] # get wife's name
            spouses = (husband_name, wife_name) # get spouses together as a tuple
            if marriage_date in spouse_date: # check if we've seen this marriage date before
                if spouses in spouse_date[marriage_date]: # check if we've seen these spouses on this date, error if so
                    self.exceptions += [f"ERROR: FAMILY: US24: [{id}] Cannot have multiple marriages with the same spouses and marriage date"]
                else: # add these spouses to this marriage date if not
                    spouse_date[marriage_date].append(spouses)
            else: # add this marriage date to the dictionary
                spouse_date[marriage_date] = [spouses]


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
    filename = "data/testfamily.ged"
    andrew_fam = Family(filename)
    andrew_fam.create_family(filename)
    print(andrew_fam)
