import pickle

nodes = pickle.load( open( 'nodelist_merged.p' , 'rb' ))

count = 0
for node in nodes:
    print
    print node
    count = count + 1
print
print "Number of nodes:\t" , count
    
