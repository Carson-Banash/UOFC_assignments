#Carson Banash (30085955)
#Lab B06

#this funciton is the function that uses nested loops
#this function determines if a given list is a sublist of another 
#the parameters are:
#Slist- this is the the smaller of the two list and the possible sublist
#Llist- this is the larger of the list and the one that is compaired to
#there is only one return, True or False, 
#that is if the smaller list is a sublist of the larger one.
def isAsublistV1(Slist, Llist):
    isSublist = False
        
    if Slist == Llist:
        isSublist = True

    else:
        for i in range(0,len(Llist)):
            if Llist[i] == Slist[0]:
                n = 1
                while (Llist[i+n] == Slist[n]) and (n < len(Slist)):
                    n += 1
                    
                    if n == len(Slist):
                        isSublist = True

    return isSublist


#this funciton is the function that uses a single loop
#this function determines if a given list is a sublist of another 
#the parameters are:
#Slist- this is the the smaller of the two list and the possible sublist
#Llist- this is the larger of the list and the one that is compaired to
#there is only one return, True or False, 
#that is if the smaller list is a sublist of the larger one.
def isAsublistV2(Slist, Llist):
    n = 0
    isSublist = False
    if Slist[0] in Llist:
        overlap_start = Llist.index(Slist[0])
    else:
        isSublist = False
    for i in range(0,len(Slist)):
        if Slist[i] in Llist:
            n += 1
            
    possible_subList = Llist[overlap_start:(overlap_start+n)]
    
    if possible_subList == Slist:
        isSublist = True

    return isSublist

def main():
    main_list = [1,5,"ACNH","NICE",56.2]
    list2 = [1,5,"NICE",56.2]
    
    if isAsublistV1(list2,main_list) == True:
        print("yes, it is a sublist")

    else:
        print("no, it is not a sublist")
main()