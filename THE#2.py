#Carson Banash (30085955)
#Lab B06

def whatType(str1, str2):
    phrase_one = str1.lower().strip(".,!?;")
    phrase_two = str2.lower().strip(".,!?;")
    is_type_A = False
    
        
    dphrase_one = {}
    dphrase_two = {}
    for char in phrase_one:
        if char in dphrase_one:
            dphrase_one[char] += 1
        else:
            dphrase_one[char] = 1
    for char in phrase_two:
        if char not in dphrase_one:
            is_type_A = False
        if char not in dphrase_two:
            dphrase_two[char] = 1
        else:
            dphrase_two[char] += 1

    if dphrase_one == dphrase_two:
        is_type_A = True
    
    if is_type_A == True:
        type_statment = str("Category A")
    else:
        type_statment = str("Category B")

    return str(type_statment)
        
#if phrase_one == phrase_two:
def main():
    str1 = "school master"
    str2 = "school master"


    print('"' + str1 + '"' + " and " + '"' + str2 + '" : ' + whatType(str1, str2))

main()