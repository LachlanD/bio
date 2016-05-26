M = 18
N = 364

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
inp = '0 87 87 99 103 113 128 128 129 129 131 147 147 147 147 186 215 216 228 234 234 242 250 257 257 273 275 278 278 285 294 344 345 356 362 362 363 370 372 381 381 404 414 420 425 425 443 473 490 491 491 492 494 501 512 517 519 528 542 567 572 590 604 619 619 620 620 623 629 629 641 648 659 666 675 698 707 716 718 732 748 751 762 767 770 776 776 788 795 797 835 845 847 854 861 863 863 875 898 898 904 917 923 926 944 948 960 964 982 985 991 1004 1010 1010 1033 1045 1045 1047 1054 1061 1063 1073 1111 1113 1120 1132 1132 1138 1141 1146 1157 1160 1176 1190 1192 1201 1210 1233 1242 1249 1260 1267 1279 1279 1285 1288 1288 1289 1289 1304 1318 1336 1341 1366 1380 1389 1391 1396 1407 1414 1416 1417 1417 1418 1435 1465 1483 1483 1488 1494 1504 1527 1527 1536 1538 1545 1546 1546 1552 1563 1564 1614 1623 1630 1630 1633 1635 1651 1651 1658 1666 1674 1674 1680 1692 1693 1722 1761 1761 1761 1761 1777 1779 1779 1780 1780 1795 1805 1809 1821 1821 1908'
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

best = 0
ans = []
for lead in leaders:
    
    cyc = lead[0][1:]
    cyc2 = cyc + cyc
    weights = []
    for i in xrange(len(cyc)):
        for j in xrange(len(cyc)):
            weights.append(sum(cyc2[i:i+j+1]))
    score = 0
    for w in spec:
        if w in weights:
            score += 1
            weights.remove(w)
            
    print lead[0], score         
    if score > best:
        best = score
        ans = cyc
        
print '-'.join(map(str,ans))
            
    

       
