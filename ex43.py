def DeBruijn2(kmers):
    d = {}
    for k in kmers:
        d.setdefault(k[:-1], []).append(k[1:])
        
    return d
    
def countBalance(d):
    ins = {}
    outs = {}
    for k,v in d.iteritems():
        outs.setdefault(k, 0)
        ins.setdefault(k, 0)
        outs[k] += len(v)
        for i in v:
            ins.setdefault(i, 0)
            outs.setdefault(i, 0) 
            ins[i] += 1
    return ins, outs
            
        
def MaximalNonBranchingPaths(d):
    ins, outs = countBalance(d)
    used = outs.copy()
    paths = []

    for k,v in d.iteritems():
        if ins[k] != 1 or outs[k] != 1:        
            for i in xrange(outs[k]):
                nonBranching = k + v[i][-1]
                nex = v[i]
                used[k] -= 1
                while ins[nex] == 1 and outs[nex] == 1:
                    used[nex] -= 1
                    nex = d[nex][0]
                    nonBranching += nex[-1]
                paths.append(nonBranching)  
    
    for k,v in d.iteritems():
        if used[k] == 1:
            path = k
            used[k] -= 1
            nex = v[0]
            while used[nex] == 1:
                path = path+nex[-1]
                used[nex] -= 1
                nex = d[nex]
            paths.append(path)       
    
    return paths
    
#f = open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_4j.txt', 'r')
f = open('C:/Users/Lachlan/Documents/GitHub/bio/temp.txt', 'r')

w = f.readlines()

f.close()

kmers = []
for line in w:
    kmers.append(line.strip('\n'))
    
db = DeBruijn2(kmers)

    
out = MaximalNonBranchingPaths(db)

    
print '\n'.join(out)

o = open('C:/Users/Lachlan/Documents/GitHub/bio/out.txt', 'w')

o.write('\n'.join(out))
o.write('\n')
    
o.close()