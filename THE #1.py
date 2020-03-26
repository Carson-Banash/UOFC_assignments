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
                """
                durring testing I found that in the following while loop the (n < len(sList))
                must come first because if it does not it results in an error because
                it tries to evalueate the list at an index that is outside of the range.
                """
                while (n < len(sList)) and (lList[i+n] == sList[n]):
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
    #sets the inital n value to zero
    n = 0
    #sets the inital booneal value of isSublist to False
    isSublist = False

    #this if statment is for determing the index where the larger loop -
    #and the first number in the smaller loop are the same
    if sList[0] in lList:
        overlap_start = lList.index(sList[0])
    #if there is no similar number then the smaller list can't be a sublist
    else:  
        isSublist = False

    #this for loop is for finding out how many elements are similar -
    #this is done so that we know how far to slice the larger loop
    for i in range(0,len(sList)):
        if sList[i] in lList:
            n += 1
    
    #this is for creating the possible sublist that would match in the larger loop -
    #this is based off of where the fist element in the smaller loop coresponds to the larger one -
    #and how many elements they have in common
    possible_subList = lList[overlap_start:(overlap_start+n)]
    
    #this says that if the smaller list and the spliced out portion of the larger list are the same -
    #then the smaller must be a sublist of the larger list
    if possible_subList == sList:
        isSublist = True #sets the isSublist value to true if the if statment is true

    #returns the boolean value for isSublist, either True or False
    return isSublist

def main():
    main_list = [1,5,"ACNH","NICE",56.2]
    list2 = [5, "ACNH"]
    
    if isAsublistV1(list2,main_list) == True:
        print("yes, it is a sublist")

    else:
        print("no, it is not a sublist")
main()