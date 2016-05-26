def DeBruijn(k, text):
    d = {}
    for i in xrange(len(text)-k+1):
        d.setdefault(text[i:i+k-1],[]).append(text[i+1:i+k])
        
    return d
    
f = open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_4c.txt', 'r')

w = f.readlines()

f.close()

k = int(w[0])
text = w[1].strip('\n')

out = DeBruijn(k, text)

o = open('C:/Users/Lachlan/Documents/GitHub/bio/out.txt', 'w')

sort = sorted(out.keys())
for key in sort:
    values = sorted(out[key])
    print key + ' -> ' + ','.join(values)
    o.write(key + ' -> ' + ','.join(values) + '\n')

    
o.close()
    