f = open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_4f.txt', 'r')

w = f.readlines()

f.close()

d = {}
for line in w:
    l = line.strip('\n').split(' -> ')
    d[int(l[0])] = [int(x) for x in l[1].strip('\n').split(',')]
    
def countBalance(d):
    bal = (max(d.keys())+1)*[0]
    for k,v in d.iteritems():
        bal[k] += len(v)
        for i in v:
            bal[i] -= 1
    return bal
        

    
        
def EulerianPath(d):
    bal = countBalance(d)
    start = bal.index(1)
    end = bal.index(-1)
    d.setdefault(end, [])
    
    stack = [start]
    out = []
    while len(stack) > 0:
        if len(d[stack[-1]]) <= 0:
            out = [stack.pop()] + out
        else:
            stack.append(d[stack[-1]].pop())
    return out
                  
    
    
out = EulerianPath(d)
print '->'.join(map(str, out))

o = open('C:/Users/Lachlan/Documents/GitHub/bio/out.txt', 'w')

o.write('->'.join(map(str, out)))
o.write('\n')
    
o.close()
