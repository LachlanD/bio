def DeBruijn3(k, kmers):
    d = {}
    for m in kmers:
        d.setdefault(m[:k-1]+m[-k-1:-1], []).append(m[1:k+1]+m[-k+1:])
        
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
            
        
def EulerianPath(d):
    bal = countBalance(d)
    for k,v in bal.iteritems():
        if v == 1:
            start = k
        if v == -1:
            end = k
    
    d.setdefault(end, [])
    
    stack = [start]
    out = []
    while len(stack) > 0:
        if len(d[stack[-1]]) <= 0:
            out = [stack.pop()] + out
        else:
            stack.append(d[stack[-1]].pop())
    return out
    
#f = open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_4i.txt', 'r')
f = open('C:/Users/Lachlan/Documents/GitHub/bio/temp.txt', 'r')


w = f.readlines()

f.close()

t = w[0].split()
k = int(t[0])
d = int(t[1])

kmers = []
for line in w[1:]:
    kmers.append(line.strip('\n'))
    
db = DeBruijn3(k, kmers)
    
out = EulerianPath(db)
string = out[0][:k-1]

for i in xrange(d+k):
    string = string + out[i+1][k-2:k-1]
for kmer in out[1:]:
    string = string + kmer[-1]
    
print string

o = open('C:/Users/Lachlan/Documents/GitHub/bio/out.txt', 'w')

o.write(string)
o.write('\n')
    
o.close()