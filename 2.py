
def akeraios(n): #opou n o arithmos pou theloume na paragontopoithei
    if n <=1000000:
        
        primes = []

        for possiblePrime in range(2, n):

            
            #ypothetoume oti o n einai prwtos
            isPrime = True
            for num in range(2, possiblePrime): #vriskoume tos prwtous arithmous mexri to n
                if possiblePrime % num == 0:
                    isPrime = False

            if isPrime:
                primes.append(possiblePrime)
            f=[]
            p=[]
            ko=[]
            newlist=[]
            div=n
            i=0
            k=0
            c=[]
            for j in range(len(primes)):
                i=i+1 #epanalipseis ises me to plithos twn prwtwn pou vrikame
                while div%primes[j]==0:
                    x=div/primes[j]
                    f.append(x)
                    p.append(primes[j]) #dimiourgia listas twvn prvtvn paragontwn tou n
                    div=x
                    for u in p:
                        if u not in newlist: #gia na min epanalambanontai oi idioi arithmoi
                            newlist.append(u)

                c=p.count(primes[j])
                ko.append(c)
                if 0 in ko:
                    ko.remove(0)

        length = len(newlist) 
        
        for w in range(length):
            print (newlist[w],'**',ko[w])


    else :
        print ("Oups number bigger than 1000000!")







akeraios(777)
