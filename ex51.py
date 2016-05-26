


f2= open('C:/Users/Lachlan/Documents/GitHub/bio/temp.txt', 'r')

w2 = f2.readlines()

f2.close()

word1 = w2[0].strip('\n')
word2 = w2[1].strip('\n')

l1 = len(word1)
l2 = len(word2)

indel = -1
score = [[0 for x in xrange(l2+1)] for y in xrange(l1+1)]

  
best = 0
besti = 0
bestj = 0    
for i in xrange(max(l1,l2)+1):
    for j in xrange(1,i+1):
        if i <= l1 and j <= l2:
            letter1 = word1[i-1]
            letter2 = word2[j-1]
            i1 = letters.index(letter1)
            i2 = letters.index(letter2)
            c = cost[i1][i2]
            score[i][j] = max(0, score[i-1][j]+indel,score[i][j-1]+indel,score[i-1][j-1]+c)
            if score[i][j] > best:
                best = score[i][j]
                besti = i
                bestj = j
        if i <= l2 and j <= l1:
            letter1 = word1[j-1]
            letter2 = word2[i-1]
            i1 = letters.index(letter1)
            i2 = letters.index(letter2)
            c = cost[i1][i2]
            score[j][i] = max(0, score[j-1][i]+indel,score[j][i-1]+indel,score[j-1][i-1]+c)
            if score[j][i] > best:
                best = score[j][i]
                besti = j
                bestj = i
i = besti
j = bestj

out1 = ''
out2 = ''

while i > 0 and j >0:
    if score[i][j] == 0:
        break
    elif score[i][j]  == score[i-1][j]+indel:
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
        
print best
print out1
print out2

o = open('C:/Users/Lachlan/Documents/GitHub/bio/out.txt', 'w')

o.write(str(best) + '\n')
o.write(out1 + '\n')
o.write(out2 + '\n')
    
o.close()