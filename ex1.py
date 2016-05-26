s = 'ACTGTACGATGATGTGTGTCAAAG'
w = 'TGT'

def Count(string, word):
    count = 0 
    start = 0
    found = True
    while found:
        index = string.find(word, start)
        if index > 0:
            start = index + 1
            count += 1
        else:
            found = False

    return count
            
print Count(s, w)