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

# Checks if files are valid in the system
def validFile(file):

    if(not os.path.isfile(file)):
        print("Error: File does not exist\n")
        return None
    if(not os.access(file, os.R_OK)):
        print("Error: File cannot be accessed\n")
        return None
    if(file[-5:] != ".json"):
        print("Error: Invalid file type\n")
        return None

    if(os.stat(file).st_size == 0):
        print("Error: File is empty\n")
        return None

    else:
        print(file, "File exists\n")

### COME BACK TO THIS IF NEEDED ###
""" def createJSON(filename):
     f = open(filename, "w")

     f.close() """

def createDict(file1, file2):
    # creates new dictionary for final DFA
    new_dict = {}
    
    # iterates through DFAs to fill out dictionary
    for i in file1:
        for j in file2:
            new_dict[i + j] = {}

            ### ENDED HERE DOO DOO ###
            if (i.type == 'start' or j.get('type') == 'start'):
                new_dict[i+j]['type'] = 'start'


    print(new_dict)
    
    return new_dict


def main():
    # gets arguments
    args = sys.argv[0:]

    # checks if DFA files are valid
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

    # closes files that were used
    f1.close()
    f2.close()



if __name__ == "__main__":
    main()