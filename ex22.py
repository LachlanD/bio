# -*- coding: utf-8 -*-

N =408
string = '0 71 71 71 97 101 103 103 113 113 115 128 128 131 137 137 156 163 163 163 168 184 186 199 208 216 227 228 234 234 240 241 252 260 264 266 268 287 287 291 305 314 319 323 331 340 347 356 362 362 365 367 371 371 388 390 390 403 415 418 420 427 436 443 450 459 459 461 468 474 484 493 503 504 518 525 528 530 533 534 542 553 555 564 574 574 578 583 587 589 596 606 622 635 637 643 658 661 667 677 679 681 681 690 691 693 696 702 711 711 737 738 750 750 752 778 780 782 794 805 806 808 814 818 821 821 824 824 830 847 849 849 851 851 865 874 895 909 920 922 924 931 936 943 945 945 948 949 952 962 968 977 977 986 1010 1014 1023 1033 1037 1046 1046 1048 1052 1057 1058 1062 1065 1073 1078 1099 1101 1108 1111 1111 1117 1136 1138 1140 1165 1165 1170 1172 1176 1177 1183 1186 1196 1209 1211 1214 1214 1236 1236 1239 1241 1254 1264 1267 1273 1274 1278 1280 1285 1285 1310 1312 1314 1333 1339 1339 1342 1349 1351 1372 1377 1385 1388 1392 1393 1398 1402 1404 1404 1413 1417 1427 1436 1440 1464 1473 1473 1482 1488 1498 1501 1502 1505 1505 1507 1514 1519 1526 1528 1530 1541 1555 1576 1585 1599 1599 1601 1601 1603 1620 1626 1626 1629 1629 1632 1636 1642 1644 1645 1656 1668 1670 1672 1698 1700 1700 1712 1713 1739 1739 1748 1754 1757 1759 1760 1769 1769 1771 1773 1783 1789 1792 1807 1813 1815 1828 1844 1854 1861 1863 1867 1872 1876 1876 1886 1895 1897 1908 1916 1917 1920 1925 1932 1946 1947 1957 1966 1976 1982 1989 1991 1991 2000 2007 2014 2023 2030 2032 2035 2047 2060 2060 2062 2079 2079 2083 2085 2088 2088 2094 2103 2110 2119 2127 2131 2136 2145 2159 2163 2163 2182 2184 2186 2190 2198 2209 2210 2216 2216 2222 2223 2234 2242 2251 2264 2266 2282 2287 2287 2287 2294 2313 2313 2319 2322 2322 2335 2337 2337 2347 2347 2349 2353 2379 2379 2379 2450'
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

spec = map(int, string.split())

total = spec[-1]

u = weight.values()


def leaderboardSequence():
    leaders = [[[0],[0],1]]
    found = False
    while(found == False):
        new_leaders = leaders[:]
        for cand in leaders:
            for v in u:
                new_pep = cand[0][:] + [v]
                new_weights = cand[1][:]
                for i in xrange(len(cand[0])):
                    sums = sum(cand[0][-1-i:])+v    
                    new_weights.append(sums)
                
                score = 0
                copy_spec = spec[:]
                for w in new_weights:
                    if w in copy_spec:
                        score += 1
                        copy_spec.remove(w)
                
                if score >= cand[2]:
                    new_leaders.append([new_pep, new_weights, score])
                    
        
        next_leaders = []
        leaders = leaders + new_leaders
        
        sort = sorted(zip(*leaders)[2])
        best = sort[-1]    
        cut = sort[-1*min(N,len(sort))]

        
        for lead in leaders:
            if lead[2]==best and lead[1][-1] == total:
                return lead[0]
            if lead[2]>=cut:
                next_leaders.append(lead)
    
        leaders = next_leaders                                                                                                  
        
                
print '-'.join(map(str,leaderboardSequence()[1:]))
            
                
                