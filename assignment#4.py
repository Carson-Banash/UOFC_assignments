#Carson Banash (30085955)
#Lab B06

#handleInput holds all of the logic for the users choice, including making sure the right extentions are present
#there are no parameters
#there are two returns, one for the input file and another for the output file name 
def handleInput():
    #asks the user for an input and sets that equal to f_In_Name
    f_In_Name = str(input("Enter the input file name: "))
    #says that if by removing the .in extention it is the same as the original, then it was never there
    if f_In_Name.rstrip(".in") == f_In_Name:
        f_In_Name += ".in"#adds the .in extention
    #creates the file out name by removing the .in extention and adding in the .out one
    f_Out_Name = f_In_Name.rstrip(".in") + ".out"
    
    #returns both the in and out file names
    return f_In_Name, f_Out_Name

#this function is resonsible for going through every word and added it to a dictinary
#there is one parameter, that being the string of text that shoul be put in the dictinary
#there is only one return, that being the dictinary made with all the word in it
def str_into_dictinary(string):
    word_count = {} #creates the dictinary
    words = string.split() #creates all of the words by splitting the orignal string
    
    #this loop goes through every word and adds it to the dictinary
    for word in words:
        word = word.lower()#sets lowercase so they are all equal to eachother
        word = word.strip(".!,?;")#cleans up the extra punctiation
        #says that if the word is in the dictinary already then increase its value by one
        if word in word_count: 
            word_count[word] += 1 #increases the words value by one
        else:
            #if the word isnt in the dictinary then it adds it with a value of one
            word_count[word] = 1 
    
    #reutrns the dictiary with the counts of each word
    return word_count

#this function is resonsible for going through the file and breaking off each paragraph,
#then it determines the words in that paragraph and the sentences.
#there are two parameters, the input file and the output file
#there are no returns, instead it writes the acording values to the output file
def paragraphwords(in_file,out_file):
    #reads the input file and strips it of extranious characters and then splits it into the paragraphs
    #it assignes a list, with the length of the number of paragraphs, to the variable whole_file_split
    whole_file_split = in_file.read().strip("\n").split("\n")
    #there are some empty elemts that show up so this is responsible for removing them
    while "" in whole_file_split:
        whole_file_split.remove("")
    #writes the total number of paragraphs to the output file. this is the length because each element of the 
    #whole_file_split is a paragraph
    out_file.write("The number of paragraphs is: " + str(len(whole_file_split))+"\n")

    #loops through each element(paragraph) of the whole_file_split list
    for i in range(0,len(whole_file_split)):
        paragraph = whole_file_split[i] #says that the paragraph is the ith element of the list
        
        #counts the number of sentences as the sum of the counts of ., !, and ?
        num_sent = paragraph.count(".") + paragraph.count("!") + paragraph.count("?")
        #writes the paragraph number to the output file, so the user knows what paragraph contains the 
        #amount of letters and sentences
        out_file.write("\nFor paragraph %s: \n" %(i+1))
        #writes the number of sentences in the ith paragraph to the output file
        out_file.write("\tnumber of sentences: " + str(num_sent)+"\n") 

        #calls the str_into_dictinary function, giving it the ith element(paragraph) to put in a dictinary
        #then it sets the returned dictianry to the variable word_count
        word_count = str_into_dictinary(whole_file_split[i])
        
        #initlizes the starting amount of words
        totNumOfWords = 0
        #loops through the words in dictinary of the ith paragraph
        for word in word_count.keys():
            #adds the coresponding count of the specific word to the total
            totNumOfWords += word_count[word]
        #writes the number of words in the ith paragraph to the output file
        out_file.write("\tThe number of words are: " + str(totNumOfWords)+"\n\n")


    
def mostAndTotalWords(in_file,out_file):

    whole_file = in_file.read().strip("\n")
    word_count = str_into_dictinary(whole_file)

    most_occurred = max(word_count.values())
    totNumOfWords = 0
    for word in word_count.keys():
        totNumOfWords += word_count[word]
        if word_count[word] == most_occurred:
            if word_count[word]>1:
                out_file.write( '"'+word+'"' + " occurred " + str(word_count[word]) + " times\n")
            else:
                out_file.write('"'+word+'"' + " occurred " + str(word_count[word]) + " time\n")

    out_file.write("Total number of words: " + str(totNumOfWords))

def main():
    in_file, out_file = handleInput()
    input_file = open(str(in_file), "r" )
    output_file = open(str(out_file), "w" )
    paragraphwords(input_file,output_file)
    input_file.close()
    output_file.close()

    input_file = open(str(in_file), "r" )
    output_file = open(str(out_file), "a" )
    mostAndTotalWords(input_file,output_file)
    input_file.close()
    output_file.close()

main()
