

f2= open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_5i.txt', 'r')

w2 = f2.readlines()

f2.close()

word1 = w2[0].strip('\n')
word2 = w2[1].strip('\n')

l1 = len(word1)
l2 = len(word2)

indel = -2

score = [[0 for x in xrange(l2+1)] for y in xrange(l1+1)]

for i in xrange(l2+1):
    score[0][i] = indel*i

  
best = 0
besti = 0
bestj = 0    
for i in xrange(max(l1,l2)+1):
    for j in xrange(1,i+1):
        if i <= l1 and j <= l2:
            if word1[i-1] == word2[j-1]:
                c =1
            else: 
                c =-2
            score[i][j] = max(indel*j, score[i-1][j]+indel,score[i][j-1]+indel,score[i-1][j-1]+c)
            
        if i <= l2 and j <= l1:
            if word1[j-1] == word2[i-1]:
                c =1
            else: 
                c =-2
            score[j][i] = max(indel*i, score[j-1][i]+indel,score[j][i-1]+indel,score[j-1][i-1]+c)
            
best = 0
index = 0
for i in xrange(l2+1):
    if score[l1][i] > best:
        best = score[l1][i] 
        index = i
        
i = l1
j = index           


out1 = ''
out2 = ''

while i > 0 and j >0:
    
    if i > 0 and score[i][j]  == score[i-1][j] + indel:
        i -= 1
        out2 = '-' + out2
        out1 = word1[i] + out1
    elif j > 0 and score[i][j] == score[i][j-1] + indel:
        j -= 1
        out1 = '-' + out1
        out2 = word2[j] + out2
    else:
        i -= 1
        j -= 1
        out1 = word1[i] + out1
        out2 = word2[j] + out2
        
print best
print out1
print out2

o = open('C:/Users/Lachlan/Documents/GitHub/bio/out.txt', 'w')

o.write(str(best) + '\n')
o.write(out1 + '\n')
o.write(out2 + '\n')
    
o.close()