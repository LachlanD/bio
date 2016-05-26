l = 12
h = 2
w = 'CTCGCACCGTTATTACGTGTGTGGTGTGTGTTATGGTGATTATGGTGATTTGCGGCTCGCACTTTGCGGGTGTGTGTTATGGTGAGTGTGTGTTTGCGGCGTTATTACCGTTATTACCGTTATTACTTATGGTGATTATGGTGACTCGCACCTCGCACTTTGCGGTTTGCGGCTCGCACTTATGGTGATTTGCGGGTGTGTGCTCGCACGTGTGTGTTTGCGGTTTGCGGCGTTATTACGTGTGTGTTTGCGGTTATGGTGATTATGGTGAGTGTGTGGTGTGTGCTCGCACCGTTATTACTTATGGTGATTTGCGGCTCGCACTTTGCGGCTCGCACCTCGCACCTCGCACTTATGGTGACTCGCACGTGTGTGCTCGCACGTGTGTGCGTTATTACCTCGCACCGTTATTACTTATGGTGATTTGCGGCTCGCACCTCGCACCGTTATTACGTGTGTGTTATGGTGATTTGCGGGTGTGTGTTATGGTGATTATGGTGATTTGCGGGTGTGTGTTTGCGGGTGTGTGTTATGGTGATTATGGTGAGTGTGTGTTATGGTGACTCGCACTTATGGTGATTTGCGGCTCGCACCTCGCACGTGTGTGTTATGGTGACGTTATTACCGTTATTACTTATGGTGATTTGCGGTTTGCGGCTCGCACTTATGGTGACGTTATTACTTATGGTGATTTGCGGGTGTGTGGTGTGTGTTTGCGGCGTTATTACCGTTATTACTTATGGTGATTATGGTGAGTGTGTGTTTGCGGTTATGGTGATTATGGTGACTCGCACTTTGCGGTTATGGTGATTATGGTGACGTTATTACGTGTGTGTTTGCGGCTCGCAC'

Map = {0:'A', 1:'C', 2:'G', 3:'T'}
Map2 = {}
Map3 = {}
count = [0]*4**l




for i in xrange(4**l):
    b = ''
    p = i
    for j in xrange(l-1,-1,-1):
        f = p/(4**j)
        b = b + Map[f]
        p = p%(4**j)
    Map2[b] = i
    Map3[i] = b



                           
      
for i in xrange(len(w)-l):
    wd = w[i:l+i]
    words = [wd]
    r=wd[::-1]
    r = r.replace('A', 'F')
    r = r.replace('T', 'A')
    r = r.replace('F', 'T')

    r = r.replace('C', 'F')
    r = r.replace('G', 'C')
    r = r.replace('F', 'G')
    rcs = [r]
    new = []
    new_rc = []
    for z in xrange(h):
    
        for word in words:
            for j in xrange(len(word)):
                new.append(word[:j] + 'A' + word[j+1:])
                new.append(word[:j] + 'C' + word[j+1:])
                new.append(word[:j] + 'G' + word[j+1:])
                new.append(word[:j] + 'T' + word[j+1:])
        words = set(new)
        
        for rc in rcs:
            for j in xrange(len(rc)):
                new_rc.append(rc[:j] + 'A' + rc[j+1:])
                new_rc.append(rc[:j] + 'C' + rc[j+1:])
                new_rc.append(rc[:j] + 'G' + rc[j+1:])
                new_rc.append(rc[:j] + 'T' + rc[j+1:])
        rcs = set(new_rc)
    
        
    for word in words:
        count[Map2[word]]  += 1   
    for rc in rcs:
        count[Map2[rc]]  += 1

m = max(count)
n = count.count(m)

ans = ''

s = 0
for i in xrange(n):
    r = count[s:].index(m)
    ans = ans + Map3[r + s] + ' '
    s = s + r + 1
     
print ans