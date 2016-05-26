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

def find_peptides(pep, existing_weight, total_weight, acc):
    
    new_acc = acc
    new_pep = pep
    for k,v in weight.iteritems():
        new_weight = existing_weight + v
        new_pep = new_pep + k
        if new_weight == total_weight:
            new_acc += 1
            #print new_pep
            print new_acc
        elif new_weight < total_weight:
            new_acc = find_peptides(new_pep,new_weight, total_weight, new_acc)
    
    return new_acc



      
    