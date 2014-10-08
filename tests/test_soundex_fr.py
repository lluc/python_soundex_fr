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
        (u"Bordeaux","BORDO"),
        (u"Bordeau","BORDO"),
        (u"Baurdox","BORDO"),
        (u"Bourges","BURJ"),
        (u"Villiers","VYLYE"),
        (u"Villers","VYLE"),
        (u"Valières","VALYERE"),
        (u"Tours","TUR"),
        (u"Jouy","JUY"),
        (u"jouais","JUE"),
        (u"Joué-les-Tours","JUELETUR"),
        (u"Été","ETE"),
        (u"Étretat","ETRETA"),
        (u"Éthretta","ETRETA"),
        (u"Allée des Granges Saint-Martin","ALEDEKRAJS1MART1"),
        (u"Rue Honoré de Balzac","RUEONOREDEBALSAK"),
        (u"Rue Emmanuel Chabrier","RUEMANUEL9ABRYE"),
        (u"Rue Barbès","RUEBARBE"),
        (u"Rue Camille Desmoulins","RUEKAMYLEDESMUL1"),
        (u"Allée des Sables","ALEDESABLE"),
        (u"Rue du Docteur Herpin","RUEDUDOKTERERP1"),
        (u"Rue Saint-Just","RUES1JU"),
        (u"Rue François Clouet","RUEFRAS2KLUE"),
        (u"Rue du Docteur Fournier","RUEDUDOKTERFURNYE"),
        (u"Rue Justin","RUEJUST1"),
        (u"Rue Pasteur","RUEPASTE"),
        (u"Rue Désiré Lecomte","RUEDESYRELEK0TE"),
        (u"Boulevard Richard Wagner","BULEVARY9ARVAJNE"),
        (u"Avenue de Grammont","AVENUEDEKRAM0"),
        (u"Avenue du Général de Gaulle","AVENUEDUJNERALDEKOLE"),
        (u"Champ Joli","9AJOLY"),
        (u"Rue Jules Taschereau","RUEJULETA9ERO"),
        (u"Groupe scolaire","KRUPESKOLERE"),
        (u"Rue de Buffon","RUEDEBUF0"),
        (u"Rue des Ursulines","RUEDERSULYNE"),
        (u"Rue Nungesser et Coli","RUEN1JSEREKOLY"),
        (u"Rue de Montbazon","RUEDEM0TBAS0"),
        (u"Le Grand Passage","LEKRAPASAJ"),
        (u"Rue du Chemin de Fer","RUEDU9EM1DEFE"),
        (u"Rue Manceau","RUEMASO"),
        (u"Rue de la Croix Nourry","RUEDELAKR2NURY"),
        (u"Pierre Armand Colin","PYEREARMAKOL1"),
        (u"Compagnons d'Emmaüs","K0PAJN0SDEMO"),
        (u"du Pont Volant","DUP0VOLAN"),
        (u"Villiers-sur-Loir","VYLYERSURL2R"),
        (u"Rue du Chemin Vert","RUEDU9EM1VER"),
    )

    def test_analyse(self):
        s = soundex_fr()
        for entree, sortie in self.valeurs :
            phonetique = s.analyse( entree.encode("UTF-8") )
            self.assertEqual( phonetique, sortie )
            
        

if __name__ == '__main__':
    unittest.main()
