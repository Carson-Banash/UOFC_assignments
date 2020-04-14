#Carson Banash (30085955)
#Lab B06

#handleInput holds all of the logic for the users choice, including making sure the right extensions are present
#there are no parameters
#there are two returns, one for the input file and another for the output file name 
def handleInput():
    #asks the user for an input and sets that equal to f_In_Name
    f_In_Name = str(input("Enter the input file name: "))
    #says that if by removing the .in extension it is the same as the original, then it was never there
    if f_In_Name.rstrip(".in") == f_In_Name:
        f_In_Name += ".in"#adds the .in extension
    #creates the file out name by removing the .in extension and adding in the .out one
    f_Out_Name = f_In_Name.rstrip(".in") + ".out"
    
    #returns both the in and out file names
    return f_In_Name, f_Out_Name

#this function is responsible for going through every word and added it to a dictionary
#there is one parameter, that being the string of text that should be put in the dictionary
#there is only one return, that being the dictionary made with all the word in it
def str_into_dictinary(string):
    word_count = {} #creates the dictionary
    words = string.split() #creates all of the words by splitting the original string
    
    #this loop goes through every word and adds it to the dictionary
    for word in words:
        word = word.lower()#sets lowercase so they are all equal to each other
        word = word.strip(".!,?;")#cleans up the extra punctuation
        #says that if the word is in the dictionary already then increase its value by one
        if word in word_count: 
            word_count[word] += 1 #increases the words value by one
        else:
            #if the word isn't in the dictionary then it adds it with a value of one
            word_count[word] = 1 
    
    #returns the dictionary with the counts of each word
    return word_count

#this function is responsible for going through the file and breaking off each paragraph,
#then it determines the words in that paragraph and the sentences.
#there are two parameters, the input file and the output file
#there are no returns, instead it writes the according values to the output file
def paragraphwords(in_file,out_file):
    #reads the input file and strips it of extraneous characters and then splits it into the paragraphs
    #it assigned a list, with the length of the number of paragraphs, to the variable whole_file_split
    whole_file_split = in_file.read().strip("\n").split("\n")
    #there are some empty elements that show up so this is responsible for removing them
    while "" in whole_file_split:
        whole_file_split.remove("")
    #writes the total number of paragraphs to the output file. this is the length because each element of the 
    #whole_file_split is a paragraph
    out_file.write("The number of paragraphs is: " + str(len(whole_file_split))+"\n")

    #loops through each element(paragraph) of the whole_file_split list
    for i in range(0,len(whole_file_split)):
        paragraph = whole_file_split[i] #says that the paragraph is the i'th element of the list
        
        #counts the number of sentences as the sum of the counts of ., !, and ?
        num_sent = paragraph.count(".") + paragraph.count("!") + paragraph.count("?")
        #writes the paragraph number to the output file, so the user knows what paragraph contains the 
        #amount of letters and sentences
        out_file.write("\nFor paragraph %s: \n" %(i+1))
        #writes the number of sentences in the i'th paragraph to the output file
        out_file.write("\tnumber of sentences: " + str(num_sent)+"\n") 

        #calls the str_into_dictinary function, giving it the i'th element(paragraph) to put in a dictionary
        #then it sets the returned dictionary to the variable word_count
        word_count = str_into_dictinary(whole_file_split[i])
        
        #initializes the starting amount of words
        totNumOfWords = 0
        #loops through the words in dictionary of the i'th paragraph
        for word in word_count.keys():
            #adds the corresponding count of the specific word to the total
            totNumOfWords += word_count[word]
        #writes the number of words in the i'th paragraph to the output file
        out_file.write("\tThe number of words are: " + str(totNumOfWords)+"\n\n")

#this function is responsible for going through the entire file 
#and determining the total words and the most common one(s)
#there are two parameters, the input file and the output file
#there are no returns, instead it writes the according values to the output file
def mostAndTotalWords(in_file,out_file):
    #reads the file and removes any extraneous characters then setting that to the variable whole_file
    whole_file = in_file.read().strip("\n")

    #calls the str_into_dictinary function, giving it the whole file to put in a dictionary
    #then it sets the returned dictionary to the variable word_count
    word_count = str_into_dictinary(whole_file)

    #determines the most occurred word as the one with the highest value
    most_occurred = max(word_count.values())

    #initializes the starting amount of words
    totNumOfWords = 0
    #loops through the words in the dictionary of the whole file
    for word in word_count.keys():
        #calculates the total amount of words as the sum of the values of each word key
        totNumOfWords += word_count[word]

    #writes the total number of all of the words to the output file
    out_file.write("Total number of words: " + str(totNumOfWords)+"\n")

    #loops through the words in dictionary of the whole file
    for word in word_count.keys():
        #this is the logic for the time vs times scenario
        #if the value of the word is equal to the value of the most occurring word then it is
        #the most occurring word
        if word_count[word] == most_occurred: 
            #if its value is greater than one then it writes that values and times to the output file
            if word_count[word]>1: 
                out_file.write( '"'+word+'"' + " occurred " + str(word_count[word]) + " times\n")
            #otherwise it prints the occurrence of the word (1) and time to the output file
            else:
                out_file.write('"'+word+'"' + " occurred " + str(word_count[word]) + " time\n")

    

#this function is responsible for the high-level processing, like the opening and closing the files
# and calling the main functions
#there are no parameters 
#there are no returns
def main():
    #sets the returns of the handleInput function, file names given by the user, to in_file and out_file
    in_file, out_file = handleInput()
    #opens the input file with the given users file name in read mode
    input_file = open(str(in_file), "r" )
    #opens the output file with the given users file name in write mode
    output_file = open(str(out_file), "w" )
    #calls the paragraphwords function giving it the input and output files
    paragraphwords(input_file,output_file)
    #closes both of the files
    input_file.close()
    output_file.close()

    '''the reason that the files are opened and closed again is because I was giving me errors if
    I didn't and the output file must be opened in append mode to avoid erasing'''
    #opens the input file with the given users file name in read mode
    input_file = open(str(in_file), "r" )
    #opens the output file with the given users file name in append mode (so it doesn't erase other work)
    output_file = open(str(out_file), "a" )
    #calls the mostAndTotalWords function giving it the input and output files
    mostAndTotalWords(input_file,output_file)
    #closes both of the files
    input_file.close()
    output_file.close()

#calls the main function to start the program
main()