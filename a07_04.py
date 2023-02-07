def devocalize(s):
    "Removes all vowels of the input strings and returns the result. Raises AttributeError if the input is not a String."
    vocals = "aeiou"
    if type(s) is str:
        for vocal in vocals:
            s = s.replace(vocal, '')
        return s
    raise AttributeError("Input was not a String")

print(devocalize("Das ist ein Baerenspass"))