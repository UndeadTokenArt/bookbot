
def get_num_of_char(path):
    with open(path) as f:
        text = f.read().lower()
        char_count = {}
        for i in text:
            if i.isalpha() == False:
                None
            elif i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1
    return char_count



# gets the number of words from a given path
def get_word_count(path):
    with open(path) as f:
        text = f.read()
        wordcount = len(text.split())
        return (str(wordcount))
    
def report():
    letter_data = get_num_of_char("books/frankenstein.txt")
    word_data = get_word_count("books/frankenstein.txt")
    l = []
    for i in letter_data:
        l.append(i)
    sorted_list = l.sort()


    print("---------- Start of report ----------")
    print(f"There are {word_data} words in the text provided")

    for i in l:
        print(f"The '{i}' character was found {letter_data[i]} times.")

    print("--------- End of report ----------")

report()