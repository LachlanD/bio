M = 20
N = 1000

weight = {'G': 57,
'A': 71,
'S': 87,
'P': 97,
'V': 99,
'T': 101,
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
inp = '0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322'
spec = map(int, inp.split())

spec.sort()
total = spec[-1]
out =[]
for i in xrange(len(spec)-1):
    for j in xrange(i+1, len(spec)):
         out.append(spec[j] - spec[i])
out = filter(lambda a: a != 0, out)

out.sort()


counts ={}
prev = out[0]
c = 1
for i in xrange(1,len(out)):
    if out[i] == prev:
        c += 1
    else:
        if prev >= 57 and prev <= 200:
            counts[prev] = c
        c = 1
        prev = out[i]
        

v = counts.values()
v.sort()


cut = v[-1*M]
con = {}
for k,v in counts.iteritems():
    if v >= cut:
        con[k] = v
    

u = con.keys()


def leaderboardSequence():
    leaders = [[[0],[0],1]]
    found = False
    out = []

    while(len(leaders)>0):
        new_leaders = []
        for cand in leaders:
            
            for v in u:
                new_pep = cand[0][:] + [v]
                new_weights = cand[1][:]
                
                
                new_weights.append(v)
                for i in xrange(len(cand[0])-1):
                    sums = sum(cand[0][-1-i:])+v    
                    new_weights.append(sums)
                
                
                score = 0
                copy_spec = spec[:]
                for w in new_weights:
                    if w in copy_spec:
                        score += 1
                        copy_spec.remove(w)
                
                new_leaders.append([new_pep, new_weights, score])
                    
        
        next_leaders = []
        leaders = new_leaders
        
        sort = sorted(zip(*leaders)[2])  
        cut = sort[-1*min(N,len(sort))]
               
        for lead in leaders:
            if lead[1][-1] == total:
                out.append(lead)
            elif lead[2]>=cut and  lead[1][-1] <= total:
                next_leaders.append(lead)
    
        leaders = next_leaders
    return out                                                                                                  
        
                
leaders = leaderboardSequence() 
scores = sorted(zip(*leaders)[2])

count =0
for lead in leaders:
    if lead[2] >= scores[-85]:
    
        count += 1
        print '-'.join(map(str,lead[0][1:]))
            
    
print count
       
