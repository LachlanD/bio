f = open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_4e.txt', 'r')

w = f.readlines()

f.close()

d = {}
for line in w:
    l = line.strip('\n').split(' -> ')
    d[int(l[0])] = [int(x) for x in l[1].strip('\n').split(',')]
    
def EulerianCycle(d):
    stack = [0]
    out = []
    while len(stack) > 0:
        if len(d[stack[-1]]) <= 0:
            out = [stack.pop()] + out
        else:
            stack.append(d[stack[-1]].pop())
    return out
                
                
    
    
out = EulerianCycle(d)
print '->'.join(map(str, out))

o = open('C:/Users/Lachlan/Documents/GitHub/bio/out.txt', 'w')

o.write('->'.join(map(str, out)))
o.write('\n')
    
o.close()
