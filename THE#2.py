#Carson Banash (30085955)
#Lab B06

def split_file(in_file):
    line = in_file.readline()
    file_list_lower = []
    file_list_regular = []
    while line != "":
        line = line.lower().strip()
        file_list_lower.append(line)
        line = in_file.readline()

    in_file.seek(0)
    line = in_file.readline()
    while line != "":
        line = line.strip()
        file_list_regular.append(line)
        line = in_file.readline()
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
        #checkes if the character is in the list of characters that are not incuded 
        #in determineing the category
        if char in bad_characters:
            #print(char, end="")
            #if the character is in the list it does nothing with it.
            #this is done so that they arent added to the dictinary
            pass 
        #checks if the character is already in the phrase one dictinary
        elif char in dphrase_one:
            #if it is in the dictinary, then its value is uncremented by one
            dphrase_one[char] += 1
        #if none of the statments above evaluate to true then it will add the character
        #to the dictinary with a value of one
        else:
            dphrase_one[char] = 1


    for char in phrase_two:
        if char in bad_characters:
            #print(char, end="")
            pass
        elif char not in dphrase_one:
            is_type_A = False
        elif char in dphrase_two:
            dphrase_two[char] += 1
        else:
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


