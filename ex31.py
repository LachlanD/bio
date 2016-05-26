def Composition(text, k):
    out = []
    for i in xrange(len(text)-k+1):
        out.append(text[i:i+k])
        
    out.sort()
    return out
        
f = open('C:/Users/Lachlan/Documents/GitHub/bio/temp.txt', 'r')

w = f.readlines()

f.close()

k = int(w[0])

text = w[1].rstrip('\n')

out = Composition(text, k)

o = open('C:/Users/Lachlan/Documents/GitHub/bio/out.txt', 'w')

for line in out:
    o.write(line + '\n')
    

o.close()