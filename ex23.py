inp = '57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493'
spec = map(int, inp.split())
spec.sort()
out =[]
for i in xrange(len(spec)-1):
    for j in xrange(i+1, len(spec)):
         out.append(spec[j] - spec[i])
out = filter(lambda a: a != 0, out)


print ' '.join(map(str,out))