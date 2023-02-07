def statistik(dateiname):
    with open(dateiname) as file:
        line = file.readline()
        stat = {}
        while (line):
            plz, name, value = line.split(';')
            if plz in stat:
                if (name in stat[plz]):
                    stat[plz][name] += int(value)
                else:
                    stat[plz][name] = int(value)
            else:
                stat[plz] = {name: int(value)}
            line = file.readline()

            
        for key in sorted(stat):
            print("{0}:".format(key), end='')
            for item in sorted(stat[key]):
                print(" {0}({1})".format(item, stat[key][item]), end='')
            print()

statistik("./bestellungen-xxx.txt")