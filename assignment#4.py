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

def paragraphwords(in_file,out_file):

    whole_file_split = in_file.read().strip("\n").split("\n")

    while "" in whole_file_split:
        whole_file_split.remove("")

    out_file.write("The number of paragraphs is: " + str(len(whole_file_split))+"\n")

    for i in range(0,len(whole_file_split)):
        paragraph = whole_file_split[i]
        
        num_sent = paragraph.count(".") + paragraph.count("!") + paragraph.count("?")
        out_file.write("\nFor paragraph %s: \n" %(i+1))
        out_file.write("\tnumber of sentences: " + str(num_sent)+"\n")

        word_count = str_into_dictinary(whole_file_split[i])
        
        totNumOfWords = 0
        for word in word_count.keys():
            totNumOfWords += word_count[word]
        
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
