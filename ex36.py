def DeBruijn2(kmers):
    d = {}
    for k in kmers:
        d.setdefault(k[:-1], []).append(k[1:])
        
    return d
    
#f = open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_4d.txt', 'r')
f = open('C:/Users/Lachlan/Documents/GitHub/bio/temp.txt', 'r')

w = f.readlines()

f.close()

kmers = []
for line in w:
    kmers.append(line.strip('\n'))
    
    
out = DeBruijn2(kmers)

o = open('C:/Users/Lachlan/Documents/GitHub/bio/out.txt', 'w')

sort = sorted(out.keys())
for key in sort:
    values = sorted(out[key])
    print key + ' -> ' + ','.join(values)
    o.write(key + ' -> ' + ','.join(values) + '\n')

    
o.close()