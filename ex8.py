w = 'GATACACTTCCCGAGTAGGTACTG'

def allSkew(w):
    s = [0]*len(w)
    for i in xrange(len(w)):
        s[i] =  w[:i+1].count('G') - w[:i+1].count('C')
        
    return s
    
def Skew(w, i):
    s = allSkew(w)
    return s[i]

def minSkew(w):
    s = allSkew(w)    
    m = min(s)
    n = s.count(m)
    start = 0
    for i in xrange(n):
        p = s[start:].index(m) + 1 + start
        print p
        start = p
        
def maxSkew(w):
    s = allSkew(w)     
    m = max(s)
    n = s.count(m)
    start = 0
    for i in xrange(n):
        p = s[start:].index(m) + 1 + start
        print p
        start = p
        
minSkew(w)