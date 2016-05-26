def d(pattern, dna):
    score = 0
    k = len(pattern)
    for s in dna:
        e =k
        for i in xrange(len(s)-k+1):
            t = 0
            for j in xrange(k):
                if not s[i+j] == pattern[j]:
                    t +=1
            e = min(t, e)
            
        score += e
    return score

    
    
def genAll(pre, allComb, length):
    if(len(pre) >= length):
        allComb.append(pre)
        return
    else:
        genAll(pre + 'A', allComb, length)
        genAll(pre + 'C', allComb, length)
        genAll(pre + 'G', allComb, length)
        genAll(pre + 'T', allComb, length)

def generatePatterns(k):
    allPatterns = []
    genAll('', allPatterns, k)
    return allPatterns
    
    
def medianString(Dna, k):
    distance = k*len(Dna)
    patterns = generatePatterns(k)
    for p in patterns:
        nd = d(p, Dna)
        if distance > nd:
            distance = nd
            median = p
    for p in patterns:
        if distance == d(p, Dna):
            print p
    return median
    
f = open('C:/Users/Lachlan/Documents/GitHub/bio/temp.txt', 'r')

w = f.readlines()

f.close()

k = int(w[0][0])

rows = []
for i in xrange(1, len(w)):
    rows.append(w[i][:-1]) 
    
out = medianString(rows, k)        

print out   