#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import os

dirname = os.path.dirname(__file__)
if dirname=='' :
    dirname='.'
dirname = os.path.realpath(dirname)
updir = os.path.split(dirname)[0]
if updir not in sys.path:
    sys.path.append(updir)

# ---------------------------------------------

from soundex_fr import soundex_fr

s = soundex_fr()

def test_analyse():
    assert s.analyse("Bordeaux") == "BORDO"
    assert s.analyse("Bordeau") == "BORDO"
    assert s.analyse("Baurdox") == "BORDO"
    assert s.analyse("Bourges") == "BURJE"
    assert s.analyse("Villiers") == "VYLYER"
    assert s.analyse("Villers") == "VYLER"
    assert s.analyse("Valières") == "VALYERE"
    assert s.analyse("Tours") == "TUR"
    assert s.analyse("Jouy") == "JUY"
    assert s.analyse("jouais") == "JUE"
    assert s.analyse("Joué-les-Tours") == "JUELETUR"
    assert s.analyse("Été") == "ETE"
    assert s.analyse("Étretat") == "ETRETA"
    assert s.analyse("Éthretta") == "ETRETA"
    
