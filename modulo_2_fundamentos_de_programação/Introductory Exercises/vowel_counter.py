words = []  # Empty list

word = input("Enter a word: ")  # Asks the user to enter a word

words.append(word)  # Adds the word to the list

print(words)  # Displays the list with the added words

# List of vowels considered, including some with accents
vowels = ["a", "ã", "â", "à", "e", "é", "ê", "è", "ë", "i", "í", "ï", "o", "ó", "ô", "õ", "ö", "u", "ú", "ù", "ü"]

# Loops through each word in the list
for word in words:
    counter = 0
    
    # Loops through each letter in the word
    for letter in word:
        
        # Converts the letter to lowercase and checks if it is in the list of vowels
        if letter.lower() in vowels:
            counter += 1  # Increments the counter if it is a vowel

    # Displays the total number of vowels found in the word
    print(f"The word {word} has {counter} vowels")
