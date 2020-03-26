#Carson Banash (30085955)
#Lab B06

#this function is the function that uses nested loops
#this function determines if a given list is a sublist of another 
#the parameters are:
#sList- this is the the smaller of the two list and the possible sublist
#lList- this is the larger of the list and the one that is compared to
#there is only one return, True or False, 
#that is if the smaller list is a sublist of the larger one.
def isAsublistV1(sList, lList):
    #sets the initial state of the isSublist to False
    isSublist = False
        
    #says that if the list are identical then the smaller list is a sublist
    if sList == lList:
        isSublist = True

    #if they aren't the same then the program will execute this code
    else:
        #runs through the numbers 0 to the length of the larger list
        for i in range(0,len(lList)):
            #if the element of the larger list at i is equal to the element of the -
            #smaller list at 0 then n is set to one and the rest of the code is executed
            if lList[i] == sList[0]:
                n = 1

                #says that while the elements of the small list and the large list, 
                #at their given indexes are the same and that the counter n is less than  -
                #the length of the smaller list then the while loop will run
                while (n < len(sList)) and (lList[i+n] == sList[n]):
                    n += 1
                    
                    #if the number of matched elements is equal to the length of the small list -
                    #then the small list is indeed a sublist of the larger
                    if n == len(sList):
                        isSublist = True #sets the value for isSublist to True

    #returns the boolean value of isSublist, either False or True
    return isSublist


#this function is the function that uses a single loop
#this function determines if a given list is a sublist of another 
#the parameters are:
#sList- this is the the smaller of the two list and the possible sublist
#lList- this is the larger of the list and the one that is compared to
#there is only one return, True or False, 
#that is if the smaller list is a sublist of the larger one.
def isAsublistV2(sList, lList):
    #sets the original boolean value for isSublist
    isSublist = False
    #initializes an empty list
    compare = []
    
    #says that if the first index value is in the larger list then to execute the code
    if sList[0] in lList:
        #gets the index in the larger list for the overlap between the two lists
        overlap_start = lList.index(sList[0]) 
        #sets the initial value for n to zero
        n = 0

        #says that while the elements of the small list and the large list, 
        #at their given indexes are the same and that the counter n is less than  -
        #the length of the smaller list then the while loop will run
        while (n < len(sList)) and (lList[overlap_start+n] == sList[n]):
            #increments the counter n by one
            n += 1
            #adds the element in the larger list into a new list to be compared later - 
            #**this is essentially splicing off the portion of the larger list that -
            #starts at the first element in the smaller list and goes for the length - 
            #of the smaller list**
            compare.append(lList[n])

            #says that once we have gone through all of the elements of the small list -
            #then we can compare the new list and the original small list
            if n == len(sList):
                #says that if the two list are the same then 
                if compare == sList:
                    isSublist = True #if they are the same then it sets the value to True

    #returns the value for isSublist, either True or False
    return isSublist
