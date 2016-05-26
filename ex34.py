def OverlapGraph(kmers):
    out = []
    for i in xrange(len(kmers)):
        for j in xrange(len(kmers)):
            if kmers[i][1:] == kmers[j][:-1]:
                out.append(kmers[i] + ' -> ' + kmers[j])
    return out
                

#f = open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_4b.txt', 'r')
f = open('C:/Users/Lachlan/Documents/GitHub/bio/temp.txt', 'r')

w = f.readlines()

f.close()

kmers = []
for line in w:
    kmers.append(line[:-1])
out = OverlapGraph(kmers)

o = open('C:/Users/Lachlan/Documents/GitHub/bio/out.txt', 'w')

for line in out:
    o.write(line + '\n')
    
o.close()
                