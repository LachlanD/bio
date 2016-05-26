string = 'TAATGCCATGGGATGTT'

k = 3
d = 2

out = []

for i in xrange(len(string)-k*2-d+1):
    out.append('('+string[i:i+k]+'|'+string[i+k+d:i+k*2+d]+')')
    
out.sort()

print ' '.join(out)