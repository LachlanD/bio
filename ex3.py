s = 'GCTAGCT'

def reverseComplement(string):
    r= string[::-1]
    r = r.replace('A', 'F')
    r = r.replace('T', 'A')
    r = r.replace('F', 'T')
    
    r = r.replace('C', 'F')
    r = r.replace('G', 'C')
    r = r.replace('F', 'G')
    
    return r

print reverseComplement(s)