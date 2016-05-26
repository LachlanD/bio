f = open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_5b.txt', 'r')

w = f.readlines()

f.close()

d= map(int, w[0].split())

down = []
right = []
i = 1
while w[i][0] != '-':
    down.append(map(int, w[i].split()))
    i += 1
   
for line in w[i+1:]:
    right.append(map(int, line.split()))


def LongestPath(m, n, down, right):
    length = [[0 for x in xrange(n+1)] for y in xrange(m+1)]
    for i in xrange(m):
        length[i+1][0] = length[i][0]+down[i][0]
    for j in xrange(n):
        length[0][j+1] = length[0][j]+right[0][j]
    
    for i in xrange(1,max(m,n)+1):

        for j in xrange(1,i+1):

            if j <= n and i <= m:
                    length[i][j] = max(length[i-1][j]+down[i-1][j], length[i][j-1]+right[i][j-1])
            if j <= m and i <= n:
                length[j][i] = max(length[j-1][i]+down[j-1][i], length[j][i-1]+right[j][i-1])

    return length[m][n]     
        
print LongestPath(d[0], d[1], down, right)