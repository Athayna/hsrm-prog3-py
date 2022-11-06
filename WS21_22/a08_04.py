def auskunft(linie, start, ziel):
    connections = []
    file = open("a08_04_fahrzeiten.txt", "r")
    line = file.readline()
    while line != '':
        if line.split(";")[0] == linie:
            connections.append(line.split(";"))
        line = file.readline()
    fahrzeit = 0
    haltestellen = []
    while True:
        for connection in connections:
            if start == ziel:
                haltestellen.append(ziel)
                return(fahrzeit, haltestellen)
            if start == connection[1]:
                fahrzeit += int(connection[3])
                haltestellen.append(start)
                start = connection[2]