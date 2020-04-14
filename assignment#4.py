def handleInput():
    f_In_Name = str(input("Enter the input file name: "))

    if f_In_Name.rstrip(".in") == f_In_Name:
        f_In_Name += ".in"
    
    f_Out_Name = f_In_Name.rstrip(".in") + ".out"
        
    return f_In_Name, f_Out_Name


def str_into_dictinary(string):
    word_count = {}
    words = string.split()
    
    for word in words:
        word = word.lower()
        word = word.strip(".!,?;")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
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
