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

def whatType(string1, string2):
    phrase_one = string1
    phrase_two = string2
    is_type_A = False
    
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
            #if both evalueate to true, then the characters value is incremented by one
            dphrase_one[char] += 1
        #if none of the statments above evaluate to true then it will add the character
        #to the dictinary with a value of one
        elif char not in dphrase_one and char not in bad_characters:
            dphrase_one[char] = 1

    #loops through all the characters in the second phrase
    for char in phrase_two:

        if char not in dphrase_one:
            is_type_A = False
        elif char in dphrase_two and char not in bad_characters:
            dphrase_two[char] += 1
        elif char not in dphrase_two and char not in bad_characters:
            dphrase_two[char] = 1

    if dphrase_one == dphrase_two:
        is_type_A = True
    
    if phrase_one == phrase_two:
        is_type_A = False
    
    if is_type_A == True:
        type_statment = "Category A"
    else:
        type_statment = "Category B"

    return type_statment
        
def main():
    input_file = open("THE2.in", "r")
    output_file = open("THE2.out", "w")

    file_list_lower, file_list_regular = split_file(input_file)
    for i in range (0,len(file_list_lower),2):
        output_file.write('"' + file_list_regular[i] + '"' + " and " + '"' + file_list_regular[i+1] + '": ' + whatType(file_list_lower[i], file_list_lower[i+1]) +"\n")

main()


