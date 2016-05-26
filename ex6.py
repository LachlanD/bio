#Find how many different k-mers appear atleast t times in a L length window of the E-coli gnome

k = 9
L = 500
t = 3

f = open('C:/Users/Lachlan/Documents/GitHub/bio/E-coli.txt', 'r')

w = f.readline()

f.close()
count = [0]*4**k

Map = {0:'A', 1:'C', 2:'G', 3:'T'}
Map2 = {}
solution = {}
      
# setup a dictionary to convert k-mers to ints
for i in xrange(4**k):
    b = ''
    p = i
    for j in xrange(k-1,-1,-1):
        l = p/(4**j)
        b = b + Map[l]
        p = p%(4**j)
    Map2[b] = i

# setup the initial L length window
for i in xrange(L-k):        
    v = (count[Map2[w[i:i+k]]] + 1)
    count[Map2[w[i:i+k]]] = v
    if v >= t:
        solution[w[i:i+k]] = True

# slide the window forward 
for i in xrange(len(w)-L):
    count[Map2[w[i:i+k]]] -= 1      
    v = (count[Map2[w[L-k+i:L+i]]] + 1)
    count[Map2[w[L-k+i:L+i]]] = v
    
    if v >= t:
        solution[w[L-k+i:L+i]] = True
        
print len(solution)