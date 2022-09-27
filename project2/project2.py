import sys
filename = "Narvaez Family v1.0.txt"
validDict = { # Valid Tags
            "INDI": 0,
            "NAME": 1,
            "SEX": 1,
            "BIRT":1,
            "DEAT":1,
            "FAMC":1,
            "FAMS":1,
            "FAM":0,
            "MARR":1,
            "HUSB":1,
            "WIFE":1,
            "CHIL":1,
            "DIV":1,
            "DATE":2,
            "HEAD":0,
            "TRLR":0,
            "NOTE":0
        } 
    
# Write to file
f = open('output.txt','w')
sys.stdout = f
        

with open(filename) as file:
    for line in file:
        line = line.rstrip()
        newLine = line.split()
        if(len(newLine) > 2 and (newLine[2] == 'INDI' or newLine[2] == 'FAM')):
            #handles when arguemnt and tag are swapped bc of exception
            newLine[1], newLine[2] = newLine[2], newLine[1]
        output = ""
        for i in range(len(newLine)):
            if i == 2:
                output += "|"
            output += newLine[i]
            if i == 0 or i == 1:
                output += "|"
                if i == 1:
                    output += "Y" if (newLine[i] in validDict and int(newLine[0]) == validDict[newLine[i]]) else "N"
            elif i >= 2:
                output += " "


        print("--> {}".format(line))
        print("<-- {}".format(output))
