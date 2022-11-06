#!/usr/bin/env python3

#
# Name: Alex Müller
# Matrikelnummer: 1259131
#



def html2java(s):
    lst = s.split("-")
    output = lst[0]
    for e in lst[1:]:
        output = output + e.capitalize()
    return output
    
    
    
def java2html(s):
    output = s[0].lower()
    for l in s[1:]:
        if l.isupper():
            output = output + "-" + l.lower()
        else:
            output = output + l
    return output



##################################################################

if __name__=="__main__":
    import unittest, sys
    assert sys.version > '3.6', 'Bitte mindestens Python 3.6 verwenden'

    class TestStringMethods(unittest.TestCase):
        """
        Automatischer Vergleich der tatsächlichen Ergebnisse
        der zu implementierenden Funktionen mit einer Referenzlösung.
        """
        def test_1(self):
            htmlname = 'admin-user-eingabe-formular'
            javaname = html2java(htmlname)
            self.assertEqual(javaname, 'adminUserEingabeFormular')

        def test_2(self):
            htmlname = 'titelseite'
            javaname = html2java(htmlname)
            self.assertEqual(javaname, 'titelseite')

        def test_3(self):
            htmlname = 'hilfe-seite'
            javaname = html2java(htmlname)
            self.assertEqual(javaname, 'hilfeSeite')

        def test_4(self):
            javaname = "navigationBar"
            htmlname = java2html(javaname)
            self.assertEqual(htmlname, "navigation-bar")

        def test_5(self):
            javaname = "titel"
            htmlname = java2html(javaname)
            self.assertEqual(htmlname, "titel")

        def test_6(self):
            javaname = "intersectionDetectionActionPanelFrameThing"
            htmlname = java2html(javaname)
            self.assertEqual(htmlname, "intersection-detection-action-panel-frame-thing")


    unittest.main()
    
