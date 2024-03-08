def count_words(file_path):
    word_count = {}
    file = open(file_path)
    for line in file:
        words = line.strip().split()
        for word in words:
            word = word.lower()
            word_count[word] = word_count.get(word, 0) + 1
    file.close()
    return word_count

def print_no_repeats(dict):
    for word in dict:
        if(dict[word] == 1):
            print(word)

word_count_dict = count_words('song.txt')
print("Dictionary:")
print(word_count_dict)
print("No repeat words:")
print_no_repeats(word_count_dict)