class Messwert:

    def __init__(self, *values) -> None:
        if len(values) == 1:
            self.zeitpunkt, self.temperatur = str(values[0]).split(',')
            self.zeitpunkt = self.zeitpunkt.strip('"')
            self.temperatur = float(self.temperatur)
        elif len(values) == 2:
            self.zeitpunkt = values[0]
            self.temperatur = values[1]
        else:
            raise ValueError("Class only accepts one or two arguments. It received {0}.".format(len(values)))

    def __str__(self) -> str:
        return '"{0}",{1}'.format(self.zeitpunkt, self.temperatur)

    def __repr__(self) -> str:
        return 'Messwert("{0}", {1})'.format(self.zeitpunkt, self.temperatur)
    
    def __eq__(self, __o: object) -> bool:
        if type(__o) is type(self):
            if self.zeitpunkt == __o.zeitpunkt and self.temperatur == __o.temperatur:
                return True
        return False

    def __lt__(self, __o: object) -> bool:
        if type(__o) is type(self):
            if self.zeitpunkt == __o.zeitpunkt:
                return self.temperatur < __o.temperatur
            return self.zeitpunkt < __o.zeitpunkt
        raise TypeError("Can't compare type Messwert to type {0}".format(type(__o)))

'''
with open("messwerte.csv") as file:
    line = file.readline()
    while line:
        mw = Messwert(line)
        if mw != eval(repr(mw)):
            print("Eval not matching for line:", line)
        line = file.readline()
'''

mw = Messwert("2013-07-15 16:03:08.260597",19.875)
mw2 = Messwert("2013-07-16 00:45:01.620453",19.125)
print(mw < mw2)