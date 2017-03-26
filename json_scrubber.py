import json

with open( 'some_tournaments.json' , 'r' ) as infile:
    some_tournaments = json.load( infile )


object_tournament_list = []

'''
for key in some_tournaments:
    for packet in some_tournaments[ key ]:
        object_tournament_list.append[ { 'roundname' : key , 'questions' : [] } ]
'''

for key in some_tournaments:

    for packet in some_tournaments[ key ]:
        
        new_packet = {}

        #print packet[ 1 ]
        new_packet[ 'roundname' ] = packet[ 0 ]
            
        tempList = []

        for question in packet[ 1 ]:
            new_question = {}
            print question
            print 
            print
            new_question[ 'prompt' ] = question[ 0 ]
            new_question[ 'answer' ] = question[ 1 ]
            
            tempList.append( new_question )

        new_packet[ 'questions' ] = tempList

        object_tournament_list.append( new_packet )


with open( 'formatted_small_tournaments.json' , 'w' ) as outfile:
    json.dump( object_tournament_list , outfile )

