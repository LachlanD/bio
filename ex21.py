inp = 'MAMA'
exp = '0 57 71 71 71 104 131 202 202 202 256 333 333 403 404'

weight = {'G': 57,
'A': 71,
'S': 87,
'P': 97,
'V':99,
'T':101,
'C': 103,
'I': 113,
'L': 113,
'N': 114,
'D': 115,
'K': 128,
'Q': 128,
'E': 129,
'M': 131,
'H': 137,
'F': 147,
'R': 156,
'Y': 163,
'W': 186}

spec = []
exp_spec = exp.split()

inp2 = inp + inp

for i in xrange(len(inp)+1):
    for j in xrange(len(inp)):
        word = inp2[j:j+i]
        total = 0
        for letter in word:
            total += weight[letter]
            
        spec.append(total)
        
#spec = list(set(spec))
spec.sort()
print ' '.join(map(str, spec[3:-3]))

score = 0

for p in spec[3:-3]:
    if str(p) in exp_spec:
        score += 1
        exp_spec.remove(str(p))

print score
