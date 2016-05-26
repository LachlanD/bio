s = 'CGCCTAAATAGCCTCGCGGAGCCTTATGCCATACTCGTCCT'
k = 3

def mostFreqKmer(string, k):
    dic = {}
    for i in xrange(len(string) - k + 1):
        
        dic[s[i:k+i]] = dic.setdefault(string[i:k+i],0) + 1
    
    m = max(dic.values())
    n = dic.values().count(m)

    p = 0
    for i in xrange(n):
        j = dic.values()[p:].index(m)
        p = j + 1
        print dic.keys()[j]
        
mostFreqKmer(s,k)