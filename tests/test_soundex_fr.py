#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import os

import unittest

dirname = os.path.dirname(__file__)
if dirname=='' :
    dirname='.'
dirname = os.path.realpath(dirname)
updir = os.path.split(dirname)[0]
if updir not in sys.path:
    sys.path.append(updir)

# ---------------------------------------------

from soundex_fr import soundex_fr



class TestFonctionAnalyse(unittest.TestCase):
    valeurs = (
        ("Bordeaux","BORDO"),
        ("Bordeau","BORDO"),
        ("Baurdox","BORDO"),
        ("Bourges","BURJ"),
        ("Villiers","VYLYE"),
        ("Villers","VYLE"),
        ("Valières","VALYERE"),
        ("Tours","TUR"),
        ("Jouy","JUY"),
        ("jouais","JUE"),
        ("Joué-les-Tours","JUELETUR"),
        ("Été","ETE"),
        ("Étretat","ETRETA"),
        ("Éthretta","ETRETA"),
        ("Allée des Granges Saint-Martin","ALEDEKRAJS1TMART1"),
        ("Rue Honoré de Balzac","RUEONOREDEBALSAK"),
        ("Rue Emmanuel Chabrier","RUEMANUEL9ABRYE"),
        ("Rue Barbès","RUEBARBE"),
        ("Rue Camille Desmoulins","RUEKAMYLEDESMUL1"),
        ("Allée des Sables","ALEDESABLE"),
        ("Rue du Docteur Herpin","RUEDUDOKTERERP1"),
        ("Rue Saint-Just","RUES1TJU"),
        ("Rue François Clouet","RUEFRAS2KLUE"),
        ("Rue du Docteur Fournier","RUEDUDOKTERFURNYE"),
        ("Rue Justin","RUEJUST1"),
        ("Rue Pasteur","RUEPASTE"),
        ("Rue Désiré Lecomte","RUEDESYRELEK0TE"),
        ("Boulevard Richard Wagner","BULEVARY9ARVAJNE"),
        ("Avenue de Grammont","AVENUEDEKRAM0"),
        ("Avenue du Général de Gaulle","AVENUEDUJNERALDEKOLE"),
        ("Champ Joli","9AJOLY"),
        ("Rue Jules Taschereau","RUEJULETA9ERO"),
        ("Groupe scolaire","KRUPESKOLERE"),
        ("Rue de Buffon","RUEDEBUF0"),
        ("Rue des Ursulines","RUEDERSULYNE"),
        ("Rue Nungesser et Coli","RUEN1JSEREKOLY"),
        ("Rue de Montbazon","RUEDEM0TBAS0"),
        ("Le Grand Passage","LEKRAPASAJ"),
        ("Rue du Chemin de Fer","RUEDU9EM1DEFE"),
        ("Rue Manceau","RUEMASO"),
        ("Rue de la Croix Nourry","RUEDELAKR2NURY"),
        ("Pierre Armand Colin","PYEREARMAKOL1"),
        ("Compagnons d'Emmaüs","K0PAJN0SDEMO"),
        ("du Pont Volant","DUP0VOLAN"),
        ("Villiers-sur-Loir","VYLYERSURL2R"),
        ("Rue du Chemin Vert","RUEDU9EM1VER"),
    )

    def test_analyse(self):
        s = soundex_fr()
        for entree, sortie in self.valeurs :
            phonetique = s.analyse( entree.decode('latin-1') )
            self.assertEqual( phonetique, sortie )
            
        

if __name__ == '__main__':
    unittest.main()
