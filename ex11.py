c = 'TGT'
w = 'CGTGACAGTGTATGGGCATCTTT'
d = 1



def ApproximatePatternCount(string, pattern, d):
    
    ans = 0
    for i in xrange(len(string)-len(pattern)+1):
        c = 0
        for j in xrange(len(pattern)):
            if not string[i+j] == pattern[j]:
                c+=1
            
        if c<= d:
            ans += 1
            
    return ans
        
print ApproximatePatternCount(w, c, d)