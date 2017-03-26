#question_parser.py       12/15/16: Ruyan Zhang
#First draft for finding links between quizbowl questions
#Used on new trier question format first
import time
import sys
import os
import re
import string
import json 
import pickle
import threading
from sortedcontainers import SortedSet

#from node_builder import makePacket
# ['answer': set() , 'keywords': set() , 'neighbors': set() , 'rank' : int] -> Node -> Packets -> Folder (or Tournament)
#
#
def main():
    
    #nodelist = [ node for packet in folder for node in packet ] 
    #os.remove( './nodelist.p' )
    #with open( 'nodelist.p' , 'w' ) as f :
    #pickle.dump( nodelist , f )
    with open( 'some_tournaments.json' , 'r' ) as data:
        all_tournaments = json.load( data )

   
    '''
    num = 1
    count = 0

    some_tournaments = {}

    for tournament in all_tournaments.keys():
        if count < num:
            some_tournaments[ tournament ] = all_tournaments[ tournament ]
            count = count + 1
        else:
            break

    '''
    #print "some_tournaments length: \t" , len( some_tournaments )
    nodelist = makeNodeList( all_tournaments )

    print nodelist

    #os.remove( './nodelist.p' )
    with open( 'nodelist_sorted_set.p' , 'w' ) as f :
        pickle.dump( nodelist , f )



    '''
    nodelist = pickle.load( open( 'nodelist.p' , 'rb' ) ) 

    #checking if the answer is another answer's keyword is pretty good!
    length = len( nodelist )
    num = 0

    answers = set()
    for node in nodelist:
        answers.add( node['raw_answer'] )

    print 'total answers: ' , length
    print 'unique answers: ' , len( answers ) 
    print '% unique answer: ' , float( len( answers )) / length * 100

    tick = time.time()
    lengthList = []

    count = 0
    for target_node in nodelist:
        count = count + 1
        lengthList.append( (len( target_node['keywords'] ), target_node['keywords'] , target_node['raw_answer'] ) )

    print lengthList
    '''

#    for item in sorted( lengthList ):
#        print item
#        print "--------------------------------"
    
#    for target_node in nodelist:
#        num += 1
#        if num % 100 == 0:
#            print str( num ) , ' / ', length 
#        if len( target_node['keywords'] ) > len( maxNode['keywords'] ) :
#            maxNode = target_node
#        for candidate_node in nodelist:
#            #if target_node['answer'] == candidate_node['answer'] and target_node != candidate_node :
#            #threshold = ( len( target_node['keywords']) + len( candidate_node['keywords']) ) / 4
#            #keywordMatch = len(target_node['keywords'] & candidate_node['keywords']) 
#            if len( target_node['answer'] & candidate_node['keywords'] ) >= 2 and not areSameNode( target_node , candidate_node ):
#                target_node['neighbors'].add( candidate_node['raw_answer'] )
#                matches += 1
#
#            #if( len( target_node['keywords'] & candidate_node['keywords'] ) >= ( (len( target_node['keywords']) + len( candidate_node['keywords']) ) / 8 ) and len( target_node['answer'] & candidate_node['answer'] ) == 0 and matches < 200 ) :
#    toc = time.time()
#
#    for node in nodelist:
#        if node['neighbors'] != set():
#            print node['raw_answer'] 
#            print node['neighbors'] 
#            print( "---------------------------------------------" )
#
#    print "maxNode:"
#    print maxNode 
#    print matches        
#    print len( nodelist )
#
#    print ( toc - tick )
#



def sameAnswerLine( node1 , node2 ):
    if node1[ 'raw_answer' ] == node2[ 'raw_answer' ]:
        return True
    
    if len( target_node['answer'] & candidate_node['keywords'] ) >= 2 and not areSameNode( target_node , candidate_node ):
        #target_node['neighbors'].add( candidate_node['raw_answer'] )
        return True
        

    return false

def areSameNode( node1 , node2 ):
    if node1['raw_answer'] != node2['raw_answer']:
        return False

    if len( node1[ 'answer' ] ) != len( node2[ 'answer' ] ):
        return False

    if node1['answer'] != node2['answer']:
        return False

    if len( node1['keywords'] ) != len( node1[ 'keywords'] ):
        return False

    elif node1['keywords'] != node2['keywords']:
        return False
    else:
        return True
#
#
def makeNodeList( tournaments ):
    
    print "Number of tournaments: \t" , len( tournaments ) 
    
    nodelist = []
    count = 0

    for key in tournaments.keys():
        print
        print
        print key
        for packet in tournaments[ key ]: #packet in tournament
            print
            print
            print packet[ 0 ]
            for question in packet[ 1 ]:
                print "Number of processed questions: \t" , count
               
                node = makeNode( question )


                if len( node[ 'answer' ] ) > 0:
                    nodelist.append( makeNode( question ) )

                count = count + 1

    return nodelist
#
#
def makeNode( question ): #depends on commonWords.p and trivialWords.p

    question_text = question[ 0 ] 
    answer_text = question[ 1 ]

    node =  {
            'answer' : parseAnswers( answer_text ) , 
            'raw_answer' : answer_text ,
            'keywords' : parseKeywords( question_text ) ,
            'neighbors' : SortedSet( [] ) ,
            'rank' : -1 
            }    

    return node

#
#
def parseKeywords( question_text ): #takes question raw text string -> set of keywords
    #   rareWords: words that don't show up in first 5000 (subject to change) most common words
    #   capWords: all capitalized words that aren't at the start of the sentence 
    commonWords = pickle.load( open( './common_word_removal/commonWords.p' , 'rb' ))   #top 7500 words
    trivialWords = pickle.load( open( './common_word_removal/trivialWords.p' , 'rb' ))    #top 48 words plus prompt and accept
    #formattedQuestion =  re.sub("[\(\[].*?[\)\]]" , " ", question_text).translate( None , "0123456789" ).replace("\n" , " ")  #regex gets rid of all things in [], like pronunciation
    formattedQuestion =  re.sub("[\(\[].*?[\)\]]" , " ", question_text).translate({ord(c): None for c in '0123456789'}).replace("\n" , " ")  #regex gets rid of all things in [], like pronunciation
    rareWords = SortedSet( [word for word in formattedQuestion.translate({ord(c): None for c in string.punctuation}).strip().split(" ") if ( word not in commonWords and word.islower())]) 
    capWords = SortedSet( word for word in re.findall( r'(?<!\.\s)\b[A-Z][a-z]*\b',  formattedQuestion ) if word.lower() not in trivialWords) 

    return capWords.union( rareWords )
# 
#
def parseAnswers( answer_text ): #similar treatment as parseKeywords
#depends on trivialWords.p
    trivialWords = pickle.load( open( './common_word_removal/trivialWords.p' , 'rb' ))    #top 48 words plus prompt and accept
    
    #formattedAnswer = set(word for word in answer_text.lower().translate( None , string.punctuation ).replace("answer" , " ").split() if word not in trivialWords )

    formattedAnswer = SortedSet(word for word in answer_text.lower().translate({ord(c): None for c in string.punctuation}).replace("answer" , " ").split() if word not in trivialWords )

    return formattedAnswer
#
#
#
#
if __name__ == '__main__': main()

