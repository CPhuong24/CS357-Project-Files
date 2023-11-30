# Author: Calvin Phuong
# Date: 11/29/2023
# Title: CS 357 Implementation Project
# Descritption: This program takes two JSON files of DFAs and returns
# the union of the two files in a single DFA in JSON format

import sys
import json
import os
#import pydot
#import graphviz

# Name: validFile
# Parameters: file - a file in the system
# Description: This function checks if the file provided exists, can be
#              accessed, is the correct file type, and if the file is empty

def validFile(file):

    if(not os.path.isfile(file)):
        print("Error: File does not exist\n")
        sys.exit()
    if(not os.access(file, os.R_OK)):
        print("Error: File cannot be accessed\n")
        sys.exit()
    if(file[-5:] != ".json"):
        print("Error: Invalid file type\n")
        sys.exit()

    if(os.stat(file).st_size == 0):
        print("Error: File is empty\n")
        sys.exit()

    else:
        print(file, "File exists\n")
        

# Name: createJSON
# Parameters: infile - a json object
# Description: This function creates a new json file with write permissions
#              and writes the infile data the new json file

def createJSON(infile):
    filename = "unioned DFA.json"
    with open(filename, "w") as outfile:
        outfile.write(infile)


    outfile.close()

def createDict(file1, file2):
    # creates new dictionary for final DFA
    new_dict = {}
    num = len(file1) * len(file2)
    
    # iterates through DFAs to create new states
    for i in file1:
        for j in file2:
            new_dict[i + j] = {}

            # adds start state for final DFA
            if (file1['q0']['start'] == 'true' and file2['q0']['start'] == 'true'):
                new_dict['q0q0']['start'] = 'true'

            # check if either DFA 1 or DFA 2 have an accepting state
            # if so, set state as accept state in final DFA
            # else, add reject state
            if (file1[i]['type'] == 'accept' or file2[j]['type'] == 'accept'):
                new_dict[i + j]['type'] = 'accept'
            else:
                new_dict[i + j]["type"] = 'reject'

            # add transitions between states 
            new_dict[i+j]['next_a'] = file1[i]['next_a'] + file2[j]['next_a']
            new_dict[i+j]['next_b'] = file1[i]['next_b'] + file2[j]['next_b']

            
    
    return new_dict

def totalStates(file1, file2):
     
     return len(file1) * len(file2)


def main():
    # gets arguments
    args = sys.argv[0:]

    # checks if DFA files are valid and are provided arguments
    if len(sys.argv) != 3:
        print('Error: Please enter 2 valid files\n')

    # continue with program
    else:

        # checks if provided files are valid
        file1 = args[1]
        validFile(file1)

        file2 = args[2]
        validFile(file2)

        # opens files to use 
        with open(file1) as f1:
            data1 = json.load(f1)
            with open(file2) as f2:
                data2 = json.load(f2)
                
                peepee = createDict(data1,data2)

                pp = json.dumps(peepee, indent = totalStates(data1,data2))
                createJSON(pp)
                print(pp)

        # closes files that were used
        f1.close()
        f2.close()



if __name__ == "__main__":
    main()