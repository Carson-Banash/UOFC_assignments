#Carson Banash (30085955)
#Lab B06

#this funciton is the function that uses nested loops
#this function determines if a given list is a sublist of another 
#the parameters are:
#sList- this is the the smaller of the two list and the possible sublist
#lList- this is the larger of the list and the one that is compaired to
#there is only one return, True or False, 
#that is if the smaller list is a sublist of the larger one.
def isAsublistV1(sList, lList):
    #sets the initial state of the isSublist to False
    isSublist = False
        
    #says that if the list are identical then the smaller list is a sublist
    if sList == lList:
        isSublist = True

    #if they areent itedical then the program will exicute this code
    else:
        #runs through the numbers 0- the lenght of the larger list
        for i in range(0,len(lList)):
            #if the element of the larger list at i is equal to the element of the -
            #smaller list at 0 then n is set to one and the rest of the code is exucted
            if lList[i] == sList[0]:
                n = 1
                
                #says that while the elements of the small list and the large list, 
                #at their given indexes are the same and that the counter n is less than  -
                #the length of the smaller list then the while loop will run
                while (lList[i+n] == sList[n]) and (n < len(sList)):
                    n += 1
                    
                    #if the number of matched elemts is equal to the length of the small list -
                    #then the small list is indeed a sublist of the larger
                    if n == len(sList):
                        isSublist = True #sets the value for isSublist to True

    #retuns the boolean value of isSublist, either False or True
    return isSublist


#this funciton is the function that uses a single loop
#this function determines if a given list is a sublist of another 
#the parameters are:
#sList- this is the the smaller of the two list and the possible sublist
#lList- this is the larger of the list and the one that is compaired to
#there is only one return, True or False, 
#that is if the smaller list is a sublist of the larger one.
def isAsublistV2(sList, lList):
    n = 0
    isSublist = False
    if sList[0] in lList:
        overlap_start = lList.index(sList[0])
    else:
        isSublist = False
    for i in range(0,len(sList)):
        if sList[i] in lList:
            n += 1
            
    possible_subList = lList[overlap_start:(overlap_start+n)]
    
    if possible_subList == sList:
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