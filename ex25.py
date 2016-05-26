f = open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_3a.txt', 'r')

w = f.readlines()

f.close()

k = int(w[0][0])
d = int(w[0][2])

i = 2
col = []
for i in xrange(1, len(w)):
    col.append(w[i][:-1])
                                                                                                                                                                                                    

def genAll(pre, allComb, length):
    if(len(pre) >= length):
        allComb.append(pre)
        return
    else:
        genAll(pre + 'A', allComb, length)
        genAll(pre + 'C', allComb, length)
        genAll(pre + 'G', allComb, length)
        genAll(pre + 'T', allComb, length)
        
def check(mot, dna, k, d):
    for i in xrange(len(dna)-k+1):
        misses = 0
        for j in xrange(k):
            if mot[j] != dna[i+j]:
                misses += 1
        if misses <= d:
            return True
    return False
        
def checkAll(mot, allDNA, k, d):
    for dna in allDNA:
        if not check(mot, dna, k, d):
            return False
    return True
    

    

comb = []
inAll = []
genAll('', comb, k)
for mot in comb:
    if checkAll(mot, col, k, d):
        inAll.append(mot)
         
print ' '.join(inAll)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  