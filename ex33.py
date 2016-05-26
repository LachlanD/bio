def Spell(kmers):
    string = kmers[0]
    for k in kmers[1:]:
        string = string + k[-1:]
    return string


f = open('C:/Users/Lachlan/Documents/GitHub/bio/dataset_198_3.txt', 'r')

w = f.readlines()

f.close()

kmers = []
for line in w:
    kmers.append(line[:-1])
    
o = open('C:/Users/Lachlan/Documents/GitHub/bio/out.txt', 'w')

o.write(Spell(kmers) + '\n')
    
o.close()
    