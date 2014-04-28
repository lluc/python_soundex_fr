#!/usr/bin/env python
# -*- coding: utf-8 -*- 


#  soundex_fr.py
#  
#  2013/10/04
#  Copyright 2013 Luc LEGER <artefacts.lle@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import re
from string import maketrans

class soundex_fr:

    def __init__(self) :
        
        # Déclaration des dictionnaires et tableaux
        
        accents_in = 'áàäâåãÁÀÄÂÅÃéèëêÉÈËÊïîìíÏÎÌÍôöòóõøÔÖÒÓÕØúùûüÚÙÛÜçÇñÑ'
        accents_out = ' a a a a a a A A A A A A-e-e-e-e E E E E i i i i I I I I o o o o o o O O O O O O u u u u U U U U s S n-N'
        self.accents = maketrans(accents_in,accents_out)

        self.conv_gu = [
            ['GUI','KI'],
            ['GUE','KE'],
            ['GR','KR'],
            ['GA','KA'],
            ['GO','KO'],
            ['GU','K'],
            ['GH','K'],
            ['GE', 'J'],
            ['SCI','SI'],
            ['SCE','SE'],
            ['CA','KA'],
            ['CL','KL'],
            ['CO','KO'],
            ['CR','KR'],
            ['CT','KT'],
            ['CU','KU'],
            ['QU','K'],
            ['Q','K'],
            ['CC','K'],
            ['CK','K'],
            ['G','J'],
            ['EST','ET'],
            ['PH','F']
        ]

        # Motifs en entrée
        self.conv_v_in = [ 'E?(AU)',
            '([EA])?[UI]([NM])([^EAIOUY]|$)',
            '[AE]O?[M]([^AEIOUY1]|$)',
            '[EA][IY]([NM]?[^NM]|$)',
            '(^|[^OEUIA])(OEU|OE|EU)([^OEUIA]|$)',
            '(OI|OY)',
            '(ILLE?|I)',
            'O(U|W)',
            'O[NM]($|[^EAOUIY])',
            '(SC|S|C)H',
            '(SC)([^EAOUIY])',
            '([^AEIOUY10])[^AEIOUYLKTPMNRD9ZBJFWVS]([UAO])([^AEIOUY])',
            '([^AEIOUY]|^)([AUO])[^AEIOUYLKTBPRSJMF]([^AEIOUY10])',
            '^KN', 
            '^PF',
            'C([^AEIOUY]|$)',
            'E(Z|R)$',
            'C', 'Z$', 'Z', 'H', 'W']
        
        # Motifs en sortie (substitution)
        self.conv_v_out = [ 'O',
            '1\\3',
            'A\\1',
            'E\\1',
            '\\1E\\3',
            '2',
            'Y',
            'U',
            '0\\1',
            '9',
            'SK',
            '\\1\\2\\3',
            '\\1\\2\\3',
            'N',
            'F',
            'K\\1',
            'E',
            'S', 'SE', 'S', '', 'V']
    
    def analyse(self,mot) :
        if mot=="" :
            return('')

        mot = mot.decode('latin-1').encode('latin-1')
        
        # Suppression des accents
        mot = mot.translate(self.accents)

        # Mettre en majuscule
        mot = mot.upper()
       
        # S muets
        p= re.compile('([A|E|I|O|U|Y|L|M|R|T])S(?:\s+|$)')
        mot = p.sub('\g<1>',mot)
        
        # T muets
        p= re.compile('([ON|US|E])T(?:\s+|$)')
        mot = p.sub('\g<1>',mot)
        
        # D muets
        p= re.compile('([AN|R])D(?:\s+|$)')
        mot = p.sub('\g<1>',mot)
        
        # P muets
        p= re.compile('([M])P(?:\s+|$)')
        mot = p.sub('\g<1>',mot)
        
        # X muets
        p= re.compile('([OI])X(?:\s+|$)')
        mot = p.sub('\g<1>',mot)
        
        # On ne garde que les lettres
        p = re.compile('[^A-Z]')
        mot = p.sub('',mot)

        # Remplacer les consonnances primaires
        for gu in self.conv_gu :
            mot = mot.replace(gu[0],gu[1])
        
        # Supprimer les lettres répétitives
        p = re.compile('(.)\\1')
        mot = p.sub('\g<1>',mot)
        
        
        # Remplacer les voyelles
        for i in range(len(self.conv_v_in)) :
            p = re.compile(self.conv_v_in[i])
            mot = p.sub(self.conv_v_out[i], mot)
            #print mot 
        # Supprimer les terminaisons T,D,X
        p = re.compile('L?[TDX]?S?$')
        mot = p.sub('', mot)
        
        return mot


if __name__ == '__main__' :
    mot = soundex_fr()
    print mot.analyse("C'est un essai de phonétique, efficace" )
