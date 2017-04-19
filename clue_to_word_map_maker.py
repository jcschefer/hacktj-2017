#clue_to_word_map_maker.py       3/25/17: Ruyan Zhang
#Reversed the structure of the json from question to clue toclue to question. This will be used to make the machine to play quizbowl

import time
import sys
import re
import string
import json
import pickle

from question_parser import areSameNode

def main():
    
    merged_list = pickle.load( open( './nodelist_sorted_set.p' , 'rb' ))

    clue_to_answer = {}

    for answer in merged_list:
        for clue in answer[ 'keywords' ]:
            if clue not in clue_to_answer:   
                clue_to_answer[ clue ].append( a
            


    

    

    
#
#
#
#
if __name__ == '__main__':
    main()
