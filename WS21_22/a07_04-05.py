def devocalize(string):
    "Removes all vowels from an input string and prints the result"
    devoc = ""
    for e in string:
        if ((e != 'a') & (e != 'e') & (e != 'i') & (e != 'o') & (e != 'u')):
            devoc = devoc + e
    print(devoc)

devocalize("Das ist ein Baerenspass")