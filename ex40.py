def DeBruijn2(kmers):
    d = {}
    for k in kmers:
        d.setdefault(k[:-1], []).append(k[1:])
        
    return d
    
def countBalance(d):
    bal = {}
    for k,v in d.iteritems():
        bal.setdefault(k, 0)
        bal[k] += len(v)
        for i in v:
            bal.setdefault(i, 0) 
            bal[i] -= 1
    return bal
            
        

def EulerianCycle(d):
    stack = [d.keys()[0]]
    out = []
    while len(stack) > 0:
        if len(d[stack[-1]]) <= 0:
            out = [stack.pop()] + out
        else:
            stack.append(d[stack[-1]].pop())
    return out
    
k = 9

kmers = []
def genKmers(kmers, s, k):
    if k == 0:
        kmers.append(s)
    else:
        genKmers(kmers, s+ '0', k-1)
        genKmers(kmers, s+ '1', k-1)

genKmers(kmers, '', k)
    

    
db = DeBruijn2(kmers)

    
out = EulerianCycle(db)
string = ''
for kmer in out[1:]:
    string = string + kmer[-1]
    
print string

o = open('C:/Users/Lachlan/Documents/GitHub/bio/out.txt', 'w')

o.write(string)
o.write('\n')
    
o.close()