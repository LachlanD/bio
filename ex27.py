def getKmers(dna, k):
    kmers = []
    for i in xrange(len(dna)-k+1):
        kmers.append(dna[i:i+k])
    return kmers
    
def getPr(kmer, prMatrix):
    pr = 1.0
    for i in xrange(len(kmer)):
         pr *= prMatrix[DNA[kmer[i]]][i]
    return pr
    
DNA = {'A':0, 'C':1, 'G':2, 'T':3}

def profile(dna, k, prMatrix):
    kmers = getKmers(dna, k)
    score = 0
    out = ''
    for kmer in kmers:
        ns = getPr(kmer, prMatrix)
        if ns > score:
            score = ns
            out = kmer
    return out
   
f = open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_3c.txt', 'r')
w = f.readlines()
f.close()

dna = w[0][:-1]
k = int(w[1])

prMatrix = []
for i in xrange(2, len(w)):
    prMatrix.append([float(x) for x in w[i][:-1].split()])
    
print profile(dna, k, prMatrix)