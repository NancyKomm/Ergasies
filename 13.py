import itertools
def maxDistance(n,a): #opou n h lista me tis apostaseis kai a o thetkos arithmos sygkrisis tous

    int (a)
    g=[]


    for L in range(0, len(n)+1):
        for subset in itertools.combinations(n, L): #euresi olwn twn pithanwn athroismatwn
            
            q=sum(subset)
            
            if q<=a: #elegxos an to athroisma einai mikrotero iso tou a
                g.append(q) #kai tote to pernaei se mia lista athroismatwn
    print (max(g)) #apo thn opoia emfanizei to megalytero egkyro
maxDistance([53,8,49],22)
