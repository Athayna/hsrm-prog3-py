import sys

def wc(path):
    count = {
        "lines": 0,
        "words": 0,
        "chars": 0,
    }
    with open(path) as file:
        line = file.readline()
        while line:
            count["lines"] += 1
            count["chars"] += len(line)
            count["words"] += len(line.split())
            line = file.readline()
    return count

#`python3 a08_03.py midsummernightdream.txt`
#compare with `wc midsummernightdream.txt`
count = wc(sys.argv[1])
print("{0} {1} {2} {3}".format(count["lines"], count["words"], count["chars"], sys.argv[1]))