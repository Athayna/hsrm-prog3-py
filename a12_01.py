import re

regexes = dict(
    Datum = re.compile(r'^(\d{2}.){2}\d{4}$'),
    EUR = re.compile(r'°(((\d{1,3}\.?\d{3})*)|(\d*)),\d{2}( EUR)?$'),
    Tel = re.compile(r'^((\+\d{1,3} )|0)$'),
    PLZ = re.compile(r'^\d{5}$'),
    Email = re.compile(r'^\w+([.-]\w+)*@\w+(-\w+)*(\.[a-z]\w+)+$'),
)

def validate_file(path):
    with open(path) as file:
        line = file.readline()
        while(line):
            key, string, truth = line.split('\t')
            truth = bool(int(truth.strip()))
            regex = regexes[key]

            try:
                assert (regex.match(string) != None) == truth
            except AssertionError:
                print("AssertionError for input: {}\n".format(string))

            line = file.readline()

validate_file('./daten-regulaere-ausdruecke.txt')