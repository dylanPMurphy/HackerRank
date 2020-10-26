

def permute( x , y , z , exclude ):

    allX = [d for d in range(x+1)]
    print(allX)
    allY = [e for e in range(y+1)]
    print(allY)
    allZ = [f for f in range(z+1)]
    print(allZ)
    all_permutations = [[a,b,c] for a in allX for b in allY for c in allZ]
    print(all_permutations)

permute(1,1,2,3)