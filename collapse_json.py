#clue_to_question_json_builder.py       3/25/17: Ruyan Zhang
#Reversed the structure of the json from question to clue to clue to question. This will be used to make the machine play quizbowl

import string
import pickle

from question_parser import areSameNode

def main():
    nodelist = pickle.load( open( './nodelist_sorted_set.p' , 'rb' ))
    
    count = 0
    
    for node1 in nodelist:
        for node2 in nodelist:
            if areSameAnswer( node1[ 'answer' ] , node2[ 'answer' ] ) and not areSameNode( node1 , node2 ):
                print '\t\t\t\t\t' , node2[ 'raw_answer' ] 
                print '\t\t\t\t\t' , node1[ 'raw_answer' ] 
                #shorter answer is kept
                node1[ 'keywords' ] = node1[ 'keywords' ].union( node2[ 'keywords' ] )
                nodelist.remove( node2 )
                    

                count = count + 1
                print "Number of nodes merged:\t" , count
    
    with open( 'nodelist_merged.p' , 'w' ) as f:
        pickle.dump( nodelist , f )
       
#
#
def areSameAnswer( a , b ):
    if( 1.0 * len( a.intersection( b ) ) / ( len( a ) + len( b ) ) > 0.35 ):
        #0.35 seems like a pretty good number
        return True
#
#

    
    

    

#
#
#
#
if __name__ == '__main__': 
    main()
