c = 'ATTCTGGA'
w = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
m = 3

ans = ''


for i in xrange(len(w)-len(c)+1):
    d = 0
    for j in xrange(len(c)):
        if not w[i+j] == c[j]:
            d+=1
        
    if d<= m:
        ans = ans + str(i) + ' '
        
print ans