a = 'CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA'
b = 'CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG'


def HammingDist(str1, str2):
    d = 0
    
    for i in xrange(len(str1)):
        if not str1[i] == str2[i]:
            d+=1
            
    return d

print HammingDist(a,b)