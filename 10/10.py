import itertools

def solve_first():
    data = open("input10.txt", "r").read().splitlines()
    tab = [int(i) for i in data]
    tab.append(max(tab)+3) #device
    tab.append(0) #charger
    tab.sort()
    print(tab)

    difference_one = 0
    difference_three = 0
    for i in range(1,len(tab)):
        if (tab[i]-tab[i-1]) == 1:
            difference_one += 1
        elif (tab[i]-tab[i-1]) == 3:
            difference_three += 1
    #ok I've noticed that all the adapters in a sorted list have
    #a difference between them equal to 1 or 3
    print("Number of elements in the table: {}".format(len(tab)) )
    print("Number of differences by one: {}".format(difference_one) )
    print("Number of differences by three: {}".format(difference_three))
    print("Product of difference: {}".format(difference_one*difference_three) )

def solve_second():
    data = open("test2.txt", "r").read().splitlines()
    tab = [int(i) for i in data]
    # tab.append(max(tab)+3) #device
    # tab.append(0) #charger
    tab.sort()
    print(tab)
    tab.insert(0,0)
    tab.insert(len(tab), max(tab) + 3)
    print(tab)
    print(len(tab))
    difference_one = 0
    difference_three = 0
    modifiable = []
    if 0 in modifiable:
        modifiable.delete(0)
    if max(tab) in modifiable:
        modifiable.delete(max(tab))

    for i in range(1,len(tab)-1):
        if ( (tab[i] - tab[i-1]) == 3) or ( (tab[i+1] - tab[i]) ) == 3:
            continue
        else:
            modifiable.append(tab[i])
        # if (tab[i]-tab[i-1]) == 1:
        #     difference_one += 1
        #     if(tab[i+1]-tab[i]) == 1:
        #         modifiable.append(tab[i])
        # elif (tab[i]-tab[i-1]) == 3:
        #     difference_three += 1
    #ok I've noticed that all the adapters in a sorted list have
    #a difference between them equal to 1 or 3
    print("Number of elements in the table: {}".format(len(tab)) )
    print("Number of differences by one: {}".format(difference_one) )
    print("Number of differences by three: {}".format(difference_three))
    print("Product of difference: {}".format(difference_one*difference_three) )
    print("modifiable:")
    print(modifiable)

    print(2**len(modifiable))

#solve_first()
solve_second()
