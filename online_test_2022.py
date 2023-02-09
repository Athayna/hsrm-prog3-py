#!/usr/bin/python3
################################################################
#
# Bitte ergaenzen Sie Ihre persoenlichen Angaben
# jeweils HINTER(!) dem Pfeil
#
# Vorname ---------> 
# Nachname --------> 
# Matrikelnummer --> 
#
# Mit der Abgabe Ihrer Loesung im versichern Sie,
# "keine unerlaubte Hilfe anderer Personen in Anspruch genommen und 
# waehrend der Pruefung mit keiner anderen Person kommuniziert zu haben. 
# Mir ist bekannt, dass eine unwahre Erklaerung rechtliche Folgen haben
# und insbesondere dazu fuehren kann, dass die Pruefung als nicht 
# bestanden bewertet wird. Mir ist auch bekannt, dass im Falle eines
# mehrfachen oder schwerwiegenden Taeuschungsversuchs die Exmatrikulation 
# moeglich ist."
# Betrugsversuche koennen auch noch verfolgt werden, wenn sie erst nach
# Veroeffentlichung der Ergebnisse bekannt werden.
# 
################################################################


################################################################
# BITTE NACHFOLGEND IHRE LOESUNG EINTRAGEN
################################################################

class RoemZahl:
    allowed_chars = {
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    def __init__(self, neo_string=""):
        if type(neo_string) is str:
            for i in range(len(neo_string)):
                if neo_string[i] not in self.allowed_chars.keys():
                    raise ValueError("String contains not allowed character: {0}".format(neo_string[i]))
                if i != 0:
                    if self.allowed_chars.get(neo_string[i]) > self.allowed_chars.get(neo_string[i-1]):
                        raise ValueError("Order incorrect: {0} can not follow on {1}".format(self.allowed_chars.get(neo_string[i]), self.allowed_chars.get(neo_string[i-1])))
            self._value = neo_string
        elif type(neo_string) is int:
            self._value = ""
            for key in self.allowed_chars.keys():
                while neo_string >= self.allowed_chars.get(key):
                    self._value += key
                    neo_string -= self.allowed_chars.get(key)
        else:
            raise ValueError("Input was not a String!")
    
    def __str__(self):
        return self._value
    
    def __repr__(self):
        return 'RoemZahl("{0}")'.format(self._value)

    def __len__(self):
        result = 0
        for char in self._value:
            result += self.allowed_chars.get(char)
        return result
    
    # TODO: fix error with 3 inputs
    def __add__(self, *other):
        for o in other:
            assert type(o) is type(self)
        new = ""
        
        for key in self.allowed_chars.keys():
            count = self._value.count(key)
            for o in other:
                count += o._value.count(key)
            while count > 0:
                new += key
                count -= 1
        
        return new


################################################################
# Einige Testfaelle zur Vor-Pruefung Ihrer Loesung
# Start durch Ausfuehrung dieses Moduls als Skript ("python3 a1.py")
# Ihre Loesung muss die Aufgabenstellung allgemein (insb. auch 
# mit anderen Werten) korrekt behandeln. Die nachfolgenden Tests
# stellen nur "Stichproben" dar und geben Hinweise auf moegliche 
# Abweichungen, sie ersetzen aber die Aufgabenstellung nicht.
################################################################


if __name__ == "__main__":
    import sys, unittest
    assert sys.version_info.major == 3, "Python3 erforderlich, Sie nutzen: %s" % sys.version

    class TestRoem_1(unittest.TestCase):
        "Instanziierung, str() und repr()"
        def test_1_1(self):
            "Parameterlose Instanziierung ist leere Ziffernfolge"
            r = RoemZahl()
            self.assertEqual('', str(r))

        def test_1_2(self):
            "Instanziierung mit zulaessiger neoroemischer Zahl"
            z = "CLVVII"
            r = RoemZahl(z)
            self.assertEqual(z, str(r))

        def test_1_3(self):
            "Repr-Darstellung muss (wie immer) ausgefuehrt wertgleiches Objekt liefern"
            z = "XXVIIII"
            r = RoemZahl(z)
            rr = repr(r)
            self.assertTrue(rr.startswith('R'))
            self.assertTrue(rr.endswith(')'))
            er = eval(rr)
            self.assertEqual(z, str(er))

    class TestRoem_2(unittest.TestCase):
        "Exception bei fehlerhaftem Zahlenformat"
        def test_2_1(self):
            "Typ unzulaessig -> Exception"
            with self.assertRaises(ValueError):
                r = RoemZahl(3.14)

        def test_2_2(self):
            "Typ unzulaessig -> Exception"
            with self.assertRaises(ValueError):
                r = RoemZahl(None)

        def test_2_3(self):
            "Fehler in Ziffern-Reihenfolge -> Exception"
            with self.assertRaises(ValueError):
                r = RoemZahl('IVVVI')

        def test_2_4(self):
            "Fehler in Ziffern-Reihenfolge -> Exception"
            with self.assertRaises(ValueError):
                r = RoemZahl('CCCLLLLXXXVXII')

        def test_2_5(self):
            "Zulaessiger groesserer Wert, also KEINE Exception"
            r = RoemZahl('CCCLLLLXXXXVII')

        def test_2_6(self):
            "Unzulaessiges Ziffernzeichen -> Exception"
            with self.assertRaises(ValueError):
                r = RoemZahl('CCLLZXVVII')


    class TestRoem_3(unittest.TestCase):
        "Neuroemische Zahlenobjekte sind addierbar und ergeben ein neues Zahlenobjekt"
        def test_3_1(self):
            "Null plus Null bleibt Null"
            z0a = RoemZahl("")
            z0b = RoemZahl()
            r =  z0a + z0b
            self.assertEqual('', str(r))
            self.assertIsNot(r, z0a)
            self.assertIsNot(r, z0b)

        def test_3_2(self):
            "57 plus 121 ist 178"
            z57  = RoemZahl("LVII")
            z121 = RoemZahl('CXVVI') 
            r = z57 + z121
            self.assertEqual('CLXVVVIII', str(r))
            self.assertIsNot(z57, r)
            self.assertIsNot(z121, r)

        def test_3_3(self):
            "Addiere 21 + 11 + 6 -> 38"
            z21 = RoemZahl('XVVI')
            z11 = RoemZahl('XI')
            z6 = RoemZahl('VI')
            r =  z21 + z11 + z6
            self.assertEqual('XXVVVIII', str(r))
            self.assertIsNot(r, z21)
            self.assertIsNot(r, z11)
            self.assertIsNot(r, z6)


    class TestRoem_4(unittest.TestCase):
        "Instanziierung mit Dezimalzahl und zurueck mit len()"
        def test_4_1(self):
            "Dezimalwert nach RoemZahl umrechnen, zunaechst mal die Null"
            r = RoemZahl(0)
            self.assertEqual('', str(r))

        def test_4_2(self):
            "Kleiner Dezimalwert ungleich Null umrechnen"
            r = RoemZahl(17)
            self.assertEqual('XVII', str(r))

        def test_4_3(self):
            "Groesseren Dezimalwert umrechnen"
            r = RoemZahl(273)
            self.assertEqual('CCLXXIII', str(r))

        def test_4_4(self):
            "len() mit einfachem Wert"
            r = RoemZahl('XVII')
            self.assertEqual(17, len(r))

        def test_4_5(self):
            "len() mit roemischer Null"
            r = RoemZahl('')
            self.assertEqual(0, len(r))

        def test_4_6(self):
            "len() mit ziemlich grosser Zahl"
            r = RoemZahl('CCLLLXXXXVVVVVIIIIIII')
            self.assertEqual(422, len(r))


    class TestRoem_5(unittest.TestCase):
        "Folgen von neoroemischen RoemZahl-Instanzen sind sortierbar"
        def test_5_1(self):
            "Drei kleine Zahlen sortieren"
            slst = sorted([RoemZahl('V'), RoemZahl('VI'), RoemZahl('IIII')])
            self.assertListEqual(['IIII','V','VI'], list(map(str, slst)))

        def test_5_2(self):
            "Verschiedene Zahlen sortieren"
            z6, z100, z5, z10 = RoemZahl('VI'), RoemZahl('C'), RoemZahl('IIIII'), RoemZahl('XVV')
            lst = [ z5, z100, z6, z10 ]
            slst = sorted(lst)
            self.assertEqual(z5, slst[0])
            self.assertEqual(z6, slst[1])
            self.assertEqual(z10, slst[2])
            self.assertEqual(z100, slst[3])

        def test_5_3(self):
            "Verschiedene Darstellungen, gleiche Gegenwerte von 17"
            lst = [RoemZahl('XVII'), RoemZahl('VIIIIIIIIIIII'), RoemZahl('VVVII'), RoemZahl('IIIIIIIIIIIIIIIII')]
            slst = sorted(lst)
            self.assertListEqual(['IIIIIIIIIIIIIIIII', 'VIIIIIIIIIIII', 'VVVII', 'XVII'], list(map(str, slst)))

        def test_5_4(self):
            "Mix aus verschiedenen Werten 5-20-20-5 und verschiedene Darstellungen gleicher Werte"
            lst = [RoemZahl('V'), RoemZahl('XX'), RoemZahl('VVVIIIII'), RoemZahl('IIIII')]
            slst = sorted(lst)
            self.assertListEqual(['IIIII', 'V', 'VVVIIIII', 'XX'], list(map(str, slst)))

        def test_5_5(self):
            "Mix aus verschiedenen Werten 17-42-17-42 und verschiedene Darstellungen gleicher Werte"
            lst = [RoemZahl('XVII'), RoemZahl('XXXVVII'), RoemZahl('VVVII'), RoemZahl('XXVVVIIIIIII')]
            slst = sorted(lst)
            self.assertListEqual(['VVVII', 'XVII', 'XXVVVIIIIIII', 'XXXVVII'], list(map(str, slst)))

    
    unittest.main(verbosity=2)


