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

def greedyMotifPseudocount(k, t, Dna):
    first = Dna[0]
    bestScore = k*t
    for i in xrange(len(first)-k+1):
        motif = [first[i:i+k]]
        prMatrix = [[1 for x in xrange(k)] for y in xrange(4)]
        for j in xrange(1, t):
            for m in xrange(k):
                prMatrix[0][m] *= float((j+3))/(j+4) 
                prMatrix[1][m] *= float((j+3))/(j+4) 
                prMatrix[2][m] *= float((j+3))/(j+4) 
                prMatrix[3][m] *= float((j+3))/(j+4) 
            
            for n in xrange(k):
                base =  DNA[motif[-1][n]]
 
                prMatrix[base][n] = prMatrix[base][n]+1.0/(j+4)
            
            
            out, score = profile(Dna[j], k, prMatrix)
            
            motif.append(out)
            
        score = scoreList(motif, k)  
        
        if score < bestScore:
            best = motif
            bestScore = score
            
      
    return best
                
f = open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_3e.txt', 'r')
w = f.readlines()
f.close()


k = int(w[0].split()[0])
t = int(w[0].split()[1])

Dna =[]
for i in xrange(1, len(w)):
    Dna.append(w[i][:-1])
    
out = greedyMotifPseudocount(k, t, Dna)

print '\n'.join(out)