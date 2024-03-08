file_path = "SMSSpamCollection.txt"

file = open(file_path)

ham_messages = []
spam_messages = []
    
for line in file:

    label, message = line.strip().split('\t')
        
    if label.lower() == 'ham':
        ham_messages.append(message)
    elif label.lower() == 'spam':
        spam_messages.append(message)

file.close()

def calculate_average(messages):
    wordsCount = 0
    for line in messages:
        words = line.strip().split()
        for word in words:
            wordsCount = wordsCount + 1
    average = wordsCount / len(messages)
    return average

def ending_with_exclamation(messages):
    count = 0
    for line in messages:
        if(line[len(line) - 1] == '!'):
            count = count + 1
    return count


average = calculate_average(ham_messages)
print("Prosjek ham poruka:")
print(average)
average = calculate_average(spam_messages)
print("Prosjek spam poruka:")
print(average)
count = ending_with_exclamation(spam_messages)
print(str(count) + " poruka zavrsava s '!'.")