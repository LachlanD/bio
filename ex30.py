import random

DNA = {'A':0, 'C':1, 'G':2, 'T':3}

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

def profile(dna, k, prMatrix):
    kmers = getKmers(dna, k)
    score = 0
    out = dna[0:k]
    for kmer in kmers:
        ns = getPr(kmer, prMatrix)
        if ns > score:
            score = ns
            out = kmer
    return out, score
    
def scoreList(motif,k):
    bestScore = len(motif)*k
    for m in motif:
        score = 0
        for n in motif:
            for i in xrange(k):
               if not m[i] == n[i]:
                   score += 1
        bestScore = min(bestScore, score)
    return bestScore
    
def randomizedMotifSearch(Dna, k, t):   
    motif = []
    for i in xrange(t):
        start = random.randint(0,len(Dna[i])-k)
        motif.append(Dna[i][start:start+k])
    bestScore = scoreList(motif,k)
    best = motif[:]
    while(True):
        prMatrix = [[1.0/(t+1) for x in xrange(k)] for y in xrange(4)]
        for j in xrange(t):
            for m in xrange(k):
                prMatrix[DNA[motif[j][m]]][m] += 1.0/(t+1)
        motif = []
        for n in xrange(t):
            new, _ = profile(Dna[n], k, prMatrix)
            motif.append(new)
        score = scoreList(motif,k)
        if score < bestScore:
            bestScore = score
            best = motif[:]
        else:
            return best, bestScore
        
        
    
        
    
    
f = open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_3g.txt', 'r')
w = f.readlines()
f.close()


k = int(w[0].split()[0])
t = int(w[0].split()[1])

Dna =[]
for i in xrange(1, len(w)):
    Dna.append(w[i][:-1])

bestScore = k*t

for j in xrange(1000):    
    out, score = randomizedMotifSearch(Dna, k, t)
    if score < bestScore:
        bestScore =score
        best = out

print '\n'.join(best)
      