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
    
string = '0 87 87 97 99 99 113 114 128 137 137 184 210 212 213 224 224 224 227 236 242 297 309 311 321 323 340 341 341 350 361 396 408 434 437 437 440 448 454 460 478 521 524 533 545 547 551 553 565 574 577 620 638 644 650 658 661 661 664 690 702 737 748 757 757 758 775 777 787 789 801 856 862 871 874 874 874 885 886 888 914 961 961 970 984 985 999 999 1001 1011 1011 1098'
spec = string.split()
total = int(spec[-1])
u = []
new_spec = spec[:]
for k, v in weight.iteritems():
    if str(v) in new_spec:
        new_spec.remove(str(v))
        if not v in u: 
            u.append(v)

out = []

def expand(current, w, spec):
    for v in u:
        new = current + [v]
        new_w = w+v
        if new_w == total:
            out.append('-'.join(str(x) for x in new))
        elif new_w < total:
            flag = True
            for p in xrange(len(current)):
                sums = sum(current[-1-p:])+v
                if not str(sums) in spec:
                    flag = False
                    break
                
            if flag:
                
                new_spec = spec[:].remove(str(v))
                expand(new, new_w, spec)
   
        
expand([], 0, spec)
print ' '.join(out)


 
              