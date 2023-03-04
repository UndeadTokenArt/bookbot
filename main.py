def get_num_of_char(path):
    with open(path) as f:
        text = f.read().lower()
        char_count = {}
        for i in text:
            if i in char_count:
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
    

letter_data = get_num_of_char("books/frankenstein.txt")
word_data = get_word_count("books/frankenstein.txt")
for i in 
