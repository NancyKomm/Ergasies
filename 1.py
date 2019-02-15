def sumIntervals(list):
    sumlist = []
    if len(list) > 0:
        for data in list:
            if len(data) == 2 and data[0] < data[1]: #elegxei an to orisma tis synartisis einai egkyro
                for i in range(data[0], data[1]):
                        sumlist.append(i) #pernaei kathe fora kai to epomeno stoixeio tis listas me epikalipsi  


            else:
                print( 'Invalid input')
                break

    else:
        return 0
    print (len(set(sumlist))) #ektiponei to teliko mikos tis listas pou thelame
sumIntervals( [[1,2], [6, 10], [11, 15] ] )
