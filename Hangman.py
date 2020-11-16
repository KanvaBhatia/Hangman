import random
word = "boomerang"
printed_letters = random.choice(list(word))
print("\nWelcome to Hangman\nCreated by - Kanva Bhatia")
def print_word():  
    for i in word:
        if i in printed_letters:
            print(i+' ', end = '')
        else:
            print('_ ', end = '')

choices = len(word) + 2
correct_letters = len(printed_letters)

print_word()
print("\n\n")

while choices > 0:
    if correct_letters == len(word):
        print("\n\n Yayayyayyayy win!!")
        break
    else:
        pass
    print("\n\n")
    print("Choices left: ", choices)
    x = input("Guess letter - ")
    printed_letters += x
    if x in word:
        correct_letters += 1
    else:
        choices -= 1
    print_word()
else:
    print("\n\nAwww.. \nYou can't even guess a simple word like ", word, "\nNo problem, some people are noobs...(ಥ _ ಥ)")
