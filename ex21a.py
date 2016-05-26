inp = 'PEEP'
exp = '0 97 129 129 129 194 226 323 323 355 452'

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

spec = [0]
exp_spec = exp.split()



for i in xrange(len(inp)):
    for j in xrange(i+1,len(inp)+1):
        word = inp[i:j]
        total = 0
        print word
        
        for letter in word:
            total += weight[letter]
            
        spec.append(total)
        
#spec = list(set(spec))
spec.sort()
print ' '.join(map(str, spec))

score = 0

for p in spec:
    if str(p) in exp_spec:
        score += 1
        exp_spec.remove(str(p))

print score