coins = [1,3,5,12,18,20]

minNumCoins = {0:0}

for i in xrange(1,17009+1):
    best = i
    for coin in coins:
        try:
            best = min(minNumCoins[i-coin], best)
        except:
            pass
        minNumCoins[i] = best +1
        
print ' '.join(map(str,minNumCoins.values()))