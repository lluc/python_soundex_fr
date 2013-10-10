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
        
        accents_in =  u'áàäâåãÁÀÄÂÅÃéèëêÉÈËÊïîìíÏÎÌÍôöòóõøÔÖÒÓÕØúùûüÚÙÛÜçÇñÑ'.encode('latin1')
        accents_out =  "aaaaaaAAAAAAeeeeEEEEiiiiIIIIooooooOOOOOOuuuuUUUUcCnN"
        self.accents = maketrans(accents_in,accents_out)

        self.conv_gu = [
            ['GUI','KI'],
            ['GUE','KE'],
            ['GA','KA'],
            ['GO','KO'],
            ['GU','K'],
            ['SCI','SI'],
            ['SCE','SE'],
            ['SC','SK'],
            ['CA','KA'],
            ['CO','KO'],
            ['CU','KU'],
            ['QU','K'],
            ['Q','K'],
            ['CC','K'],
            ['CK','K'],
            ['G','J'],
            ['ST','T'],
            ['PH','F']
        ]

        self.conv_v_in = [ 'E?(AU)', '([EA])?[UI]([NM])([^EAIOUY]|$)',
            '[AE]O?[NM]([^AEIOUY]|$)',
            '[EA][IY]([NM]?[^NM]|$)',
            '(^|[^OEUIA])(OEU|OE|EU)([^OEUIA]|$)',
            'OI',
            '(ILLE?|I)', 'O(U|W)', 'O[NM]($|[^EAOUIY])', '(SC|S|C)H',
            '([^AEIOUY1])[^AEIOUYLKTPNRD]([UAO])([^AEIOUY])',
            '([^AEIOUY]|^)([AUO])[^AEIOUYLKTPR]([^AEIOUY1])', '^KN', 
            '^PF', 'C([^AEIOUY]|$)',  'E(Z|R)$',
            'C', 'Z$', '(?<!^)Z+', 'H', 'W']

        self.conv_v_out = [ 'O', '1\\3', 'A\\1',
            'E\\1', '\\1E\\3', 'O',
            'Y', 'U', 'O\\1', '9',
            '\\1\\2\\3', '\\1\\2\\3', 'N',
            'F', 'K\\1', 'E',
            'S', 'SE', 'S', '', 'V']
    
    def analyse(self,mot) :
        if mot=="" :
            return('')
        mot = mot.decode('utf-8').encode('latin1')
        
        # Suppression des accents
        mot = mot.translate(self.accents)
        
        # Mettre en majuscule
        mot = mot.upper()
        
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
        
        # Supprimer les terminaisons T,D,X,S
        p = re.compile('L?[TDX]?S?$')
        mot = p.sub('', mot)
        
        return mot


if __name__ == '__main__' :
    mot = soundex_fr()
    print mot.analyse("C'est un essai de phonétique, efficace")
