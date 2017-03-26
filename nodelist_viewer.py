import pickle

nodes = pickle.load( open( 'nodelist_sorted_set.p' , 'rb' ))

for node in nodes:
    print
    print node
    
