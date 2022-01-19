class Messwert:
    def __init__(self, *element):
        lst = list(element)
        if(element.count > 1):
            self.zeitpunkt = element
            self.temperatur = element
        
print(5)