import pickle

words = list( open( 'words10k.txt' ).readlines() )
word_list = []

for i in range( 100 ):
    word_list.append( words[ i ] )

with open( 'trivialWords.p' , 'w' ) as f:
    pickle.dump( set( word_list ) , f )
    
