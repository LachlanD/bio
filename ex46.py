f = open('C:/Users/Lachlan/Documents/GitHub/bio/temp.txt', 'r')

w = f.readlines()

f.close()

string1 = w[0].strip('\n')
string2 = w[1].strip('\n')
l1 = len(string1)
l2 = len(string2)

matches = [[0 for x in string2] for y in string1]
for i in xrange(l1):
    for j in xrange(l2):
        if string1[i] == string2[j]:
            matches[i][j] = 1
            
score = [[0 for x in xrange(l2+1)] for y in xrange(l1+1)]
for i in xrange(max(l1,l2)+1):
    for j in xrange(1,i+1):
        if i <= l1 and j <= l2:
            score[i][j] = max(score[i-1][j],score[i][j-1],score[i-1][j-1]+matches[i-1][j-1])
        if i <= l2 and j <= l1:
            score[j][i] = max(score[j-1][i],score[j][i-1],score[j-1][i-1]+matches[j-1][i-1])

         
def outputLCS(i, j, score, string):
    out = ''
    while i > 0 and j > 0:
        if score[i-1][j] == score[i][j]:
            i -= 1
        elif score[i][j-1] == score[i][j]:
            j-=1
        else:
            out = string[i-1]+out
            i-=1
            j-=1
    return out
    

o = outputLCS(l1,l2,score, string1)
print o