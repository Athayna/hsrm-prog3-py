def auskunft(linie, start, ziel):
    with open("fahrzeiten.txt") as file:
        if start == ziel:
            return (0, [start])
        weg = [start]
        zeit = 0
        lines = file.readlines()
        while start != ziel:
            for line in lines:
                vehicle, current_halt, next_halt, time = line.split(';')
                time = int(time.strip())
                if len(weg) == 0:
                    if (vehicle == linie) and (current_halt == start):
                        zeit += time
                        start = next_halt
                        weg.append(start)
                else:
                    if current_halt == start:
                        zeit += time
                        start = next_halt
                        weg.append(start)
                if start == ziel:
                    break
        return (zeit, weg)

minuten, weg = auskunft("S9", "Kelsterbach", "Niederrad")
print(minuten, " Minuten so: ", weg)