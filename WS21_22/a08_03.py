import sys

def zaelen(file):
    file = open(file).read()
    words = 1
    letters = 0
    for letter in file:
        if (letter in (" ", '\n', '\t')):
            words += 1
        letters += 1
    print("Words: " + str(words) + " Letters: " + str(letters))

file = sys.argv[1]
#file = "a08_03.txt"
zaelen(file)