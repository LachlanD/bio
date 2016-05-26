def Reconstruct(kmers):
    for k in kmers:
        copy = kmers[:]
        copy.remove(k)
        out = recon_rec(k, copy)
        if not out == '':
            return out
    
    
def recon_rec(string, kmers):
    # print string, kmers
    if kmers == []:
        return string
    
    for k in kmers:
        # print k[:-1],string[(-len(k)+1):], string[:-1] + k[-2:]
        copy = kmers[:]
        copy.remove(k)
        if k[:-1] == string[(-len(k)+1):]:
            out = recon_rec(string[:-1] + k[-2:], copy)
            if not out == '': 
                return out
    return '' 
            
            
f = open('C:/Users/Lachlan/Documents/GitHub/bio/temp.txt', 'r')

w = f.readlines()

f.close()

kmers = []
for line in w:
    kmers.append(line[:-1])
    
print Reconstruct(kmers)