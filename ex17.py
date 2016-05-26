f = open('C:/Users/Lachlan/Documents/GitHub/bio/B_brevis.txt', 'r')

string =''

f.close()


pep = 'CYCLIC'

table = {'AAA': 'K',
'AAC': 'N',
'AAG': 'K',
'AAU': 'N',
'ACA': 'T',
'ACC': 'T',
'ACG': 'T',
'ACU': 'T',
'AGA': 'R',
'AGC': 'S',
'AGG': 'R',
'AGU': 'S',
'AUA': 'I',
'AUC': 'I',
'AUG': 'M',
'AUU': 'I',
'CAA': 'Q',
'CAC': 'H',
'CAG': 'Q',
'CAU': 'H',
'CCA': 'P',
'CCC': 'P',
'CCG': 'P',
'CCU': 'P',
'CGA': 'R',
'CGC': 'R',
'CGG': 'R',
'CGU': 'R',
'CUA': 'L',
'CUC': 'L',
'CUG': 'L',
'CUU': 'L',
'GAA': 'E',
'GAC': 'D',
'GAG': 'E',
'GAU': 'D',
'GCA': 'A',
'GCC': 'A',
'GCG': 'A',
'GCU': 'A',
'GGA': 'G',
'GGC': 'G',
'GGG': 'G',
'GGU': 'G',
'GUA': 'V',
'GUC': 'V',
'GUG': 'V',
'GUU': 'V',
'UAA': '',
'UAC': 'Y',
'UAG': '',
'UAU': 'Y',
'UCA': 'S',
'UCC': 'S',
'UCG': 'S',
'UCU': 'S',
'UGA': '',
'UGC': 'C',
'UGG': 'W',
'UGU': 'C',
'UUA': 'L',
'UUC': 'F',
'UUG': 'L',
'UUU': 'F'}

out = []

m = string.replace('T', 'U')

r = string[::-1]
r = r.replace('A', 'F')
r = r.replace('T', 'A')
r = r.replace('F', 'T')

r = r.replace('C', 'F')
r = r.replace('G', 'C')
r = r.replace('F', 'G')

rm = r.replace('T', 'U')

n = len(pep)*3

count = 0

for i in xrange(len(m)-n+1):
    pr = ''
    rcpr = ''
    for j in xrange(n/3):
        pr = pr + table[m[i+j*3:i+j*3+3]]
        rcpr = rcpr + table[rm[i+j*3:i+j*3+3]]
        
        
    if pr == pep:
        #print string[i:i+n]
        count += 1
    if rcpr == pep:
        #print string[len(m)-i-n:len(m)-i]
        count += 1

print count