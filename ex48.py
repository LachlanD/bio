f1 = open('C:/Users/Lachlan/Documents/GitHub/bio/BLOSUM62.txt', 'r')

w1 = f1.readlines()

f1.close()
letters = w1[0].split()

cost = []
for line in w1[1:]:
    cost.append(map(int, line.split()[1:]))

f2= open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_5e.txt', 'r')

w2 = f2.readlines()

f2.close()

word1 = w2[0].strip('\n')
word2 = w2[1].strip('\n')

l1 = len(word1)
l2 = len(word2)

indel = -5

score = [[0 for x in xrange(l2+1)] for y in xrange(l1+1)]


for i in xrange(l2+1):
    score[0][i] = indel*i
    
for i in xrange(l1+1):
    score[i][0] = indel*i    
    
for i in xrange(max(l1,l2)+1):
    for j in xrange(1,i+1):
        if i <= l1 and j <= l2:
            letter1 = word1[i-1]
            letter2 = word2[j-1]
            i1 = letters.index(letter1)
            i2 = letters.index(letter2)
            c = cost[i1][i2]
            score[i][j] = max(score[i-1][j]+indel,score[i][j-1]+indel,score[i-1][j-1]+c)
        if i <= l2 and j <= l1:
            letter1 = word1[j-1]
            letter2 = word2[i-1]
            i1 = letters.index(letter1)
            i2 = letters.index(letter2)
            c = cost[i1][i2]
            score[j][i] = max(score[j-1][i]+indel,score[j][i-1]+indel,score[j-1][i-1]+c)
i = l1
j = l2

out1 = ''
out2 = ''

while i > 0 and j >0:
    if score[i][j]  == score[i-1][j]+indel:
        i -= 1
        out2 = '-' + out2
        out1 = word1[i] + out1
    elif score[i][j] == score[i][j-1] + indel:
        j -= 1
        out1 = '-' + out1
        out2 = word2[j] + out2
    else:
        i -= 1
        j -= 1
        out1 = word1[i] + out1
        out2 = word2[j] + out2
        
while i > 0:
    i -= 1
    out2 = '-' + out2
    out1 = word1[i] + out1
    
while j > 0:
    j -= 1
    out1 = '-' + out1
    out2 = word2[j] + out2
    
print score[l1][l2]
print out1
print out2

o = open('C:/Users/Lachlan/Documents/GitHub/bio/out.txt', 'w')

o.write(str(score[l1][l2]) + '\n')
o.write(out1 + '\n')
o.write(out2 + '\n')
    
o.close()