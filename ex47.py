f = open('C:/Users/Lachlan/Documents/GitHub/bio/rosalind_5d.txt', 'r')

w = f.readlines()

f.close()

start = int(w[0])
end = int(w[1])


graph ={}
for line in w[2:]:
    l1 = line.split('->')
    head = int(l1[0])
    l2 = l1[1].split(':')
    tail = int(l2[0])
    score = int(l2[1])
    graph.setdefault(head, []).append([tail, score])
    
scores = {start: 0}
backtrack = {}

def calc(current, graph, score, backtrack, end):
    if current == end:
        return
    for node in graph.get(current,[]):

        if score.get(node[0], 0) < score[current]+node[1]:
            score[node[0]] = score[current]+node[1]
            backtrack[node[0]] = current
            calc(node[0], graph, score, backtrack, end)
        
calc(start, graph, scores, backtrack, end)

def back(start, current, backtrack, string):
    if current == start:
        return str(start) + string
    return back(start, backtrack[current], backtrack, '->' + str(current) + string)

out = back(start, end, backtrack, '')

print scores[end]
print out
    

