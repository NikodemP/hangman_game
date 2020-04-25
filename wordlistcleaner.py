# Function cleaning the given wordlits from words with '(' or ')'.
# For example in this folder we have txt file 'wordlist.txt'.



outFile = 'cleaned_wordlist.txt'


def clean_wordlist():
    inFile = input('Enter the name of the text file to clean: ')
    # Open given file for read only.
    fin = open(inFile, "r")
    # Create a new file for selected words.
    fout = open(outFile, "w+")

    # Look for words with parenthesis in it and skip it.
    for word in fin:
        if '(' in word or ')' in word:
            continue
        # Write not skipped words into new file.
        fout.write(word)

    # Close all files
    fin.close()
    fout.close()


clean_wordlist()
