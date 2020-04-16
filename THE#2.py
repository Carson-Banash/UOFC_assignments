#Carson Banash (30085955)
#Lab B06


#this funciton is responsible for taking the whole file and spliting it into two different lists,
#each element of that list is one whole line from the file. The reason that it is two list is,
#that one file contains the lowercase of the file and the other contains the original file. 
#The lower case one is for determieing what categroy the two phrases fit into while the other one
#is used for writing the orignal prases to the file unaltered. 
#there is one paramater, that being the whole file 
#there are two returns, the list of the file in lowercase and the list of the file in its original form 
def split_file(in_file):
    #sets the variable line to the first line in the file given to the function
    line = in_file.readline()
    #initilizes both of the lists
    file_list_lower = []
    file_list_regular = []

    #says that while there is still characters in the variable line to continue looping
    while line != "":
        #sets all of the characters to lowercase and strips any extranious characters off the line
        line = line.lower().strip()
        #appends the lowered and striped line to the altered version of the list 
        file_list_lower.append(line)
        #sets the line to the next line in the file, this is needed so the file is looped through
        line = in_file.readline()

    #starts at the begging of the file again
    in_file.seek(0)
    #sets the variable line to the first line in the file 
    line = in_file.readline()
    #says that while there is still characters in the varible line to contine looping
    while line != "":
        #this time it only strips an extranious character off the line
        line = line.strip()
        #appends the striped line to the unaltered version of the list
        file_list_regular.append(line)
        #sets the line to the next line in the file, this is needed so the file is looped through
        line = in_file.readline()

#the function returs the list of the file in lowercase and the original, each element being a line from the file
    return file_list_lower, file_list_regular

#this function is responsible for adding each character of two given strings to its own dictinary.
#however, it doesnt add punctiation or spaces to the dicinaries
#there are two paramaters, they are both of the stings to be compaired
#there is one return, that being a sting that either says the stings are part of categorie A of B 
def whatCategory(string1, string2):
    #sets phrase one and two to the two strings given to the function
    phrase_one = string1
    phrase_two = string2
    #sets the initial boolean value of is_category_A to false
    is_category_A = False
    
    #a list of characters that are not used in determining the category
    bad_characters = [".", ",", " ", "-", "?", "!"]

    #initlizes both of the dictinaries for the two phrases 
    dphrase_one = {}
    dphrase_two = {}

    #loops through all the characters in the first phrase
    for char in phrase_one:
        #checks if the character is already in the phrase one dictinary and if its not in the 
        #bad characters list
        if char in dphrase_one and char not in bad_characters:
            #if both statmets in the if statment evaluate to true, 
            #then the characters value is incremented by one
            dphrase_one[char] += 1
        #checks if the character is not alerady in the pharse one dictinary and if its not in the 
        #bad characters list
        elif char not in dphrase_one and char not in bad_characters:
            #if none of the statments above evaluate to true then it will add the character
            #to the dictinary with a value of one
            dphrase_one[char] = 1

    #loops through all the characters in the second phrase
    for char in phrase_two:
        #says that if the character is not in the dictinary of the first phrase
        #the two phases are not in category A 
        if char not in dphrase_one:
            is_category_A = False
        #checks if the character is already in the phrase two dictinary and if its not in the 
        #bad characters list
        elif char in dphrase_two and char not in bad_characters:
            #if both statmets in the if statment evaluate to true, 
            #then the characters value is incremented by one
            dphrase_two[char] += 1
        #checks if the character is not alerady in the pharse one dictinary and if its not in the 
        #bad characters list
        elif char not in dphrase_two and char not in bad_characters:
            #if none of the statments above evaluate to true then it will add the character
            #to the dictinary with a value of one
            dphrase_two[char] = 1

    #says that if the two dictinarys are the same then the two phrases are in category A
    if dphrase_one == dphrase_two:
        is_category_A = True
    
    #says that if the two strings are the same then the two phrases are not in category A
    #this is because they are in the same order which mean that they are category B
    if phrase_one == phrase_two:
        is_category_A = False
    
    #says that if the boolean value for is_category_A is true then the two stings are in category A
    if is_category_A == True:
        #sets the category statment to A
        category_statment = "Category A"
    #if the boolean value for is_category_A is not true (false) then its category B
    else:
        #sets the category statment to B
        category_statment = "Category B"

    #returns the category statment, either A or B
    return category_statment
        
def main():
    input_file = open("THE2.in", "r")
    output_file = open("THE2.out", "w")

    file_list_lower, file_list_regular = split_file(input_file)
    for i in range (0,len(file_list_lower),2):
        output_file.write('"' + file_list_regular[i] + '"' + " and " + '"' + file_list_regular[i+1] + '": ' + whatCategory(file_list_lower[i], file_list_lower[i+1]) +"\n")

main()


