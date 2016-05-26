k = 4
L = 30
t = 3


w = 'GCACAAGGCCGACAATAGGACGTAGCCTTGAAGACGACGTAGCGTGGTCGCATAAGTACAGTAGATAGTACCTCCCCCGCGCATCCTATTATTAAGTTAATT'


sol =  {}
dic = {}  

for j in xrange(L-k):
    dic[w[j:k+j]] = dic.setdefault(w[j:k+j],0) + 1

for i in xrange(len(w)-L-k):

    dic[w[i:k+i]] = dic[w[i:k+i]] - 1
    dic[w[i+L-k:i+L]] = dic.setdefault(w[i+L-k:i+L],0) + 1
    
        
    for key, elem in dic.items():
        if elem >= t:
            sol[key] = True
            
print ' '.join(sol.keys())
print len(sol)