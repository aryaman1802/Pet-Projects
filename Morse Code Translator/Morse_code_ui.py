#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 04:57:07 2022

@author: aryaman
"""

morse = {
    'A' : '● ▬',
    'B' : '▬ ● ● ●',
    'C' : '▬ ● ▬ ●',
    'D' : '▬ ● ●',
    'E' : '●',
    'F' : '● ● ▬ ●',
    'G' : '▬ ▬ ●',
    'H' : '● ● ● ●',
    'I' : '● ●',
    'J' : '● ▬ ▬ ▬',
    'K' : '▬ ● ▬',
    'L' : '● ▬ ● ●',
    'M' : '▬ ▬',
    'N' : '▬ ●',
    'O' : '▬ ▬ ▬',
    'P' : '● ▬ ▬ ●',
    'Q' : '▬ ▬ ● ▬',
    'R' : '● ▬ ●',
    'S' : '● ● ●',
    'T' : '▬',
    'U' : '● ● ▬',
    'V' : '● ● ● ▬',
    'W' : '● ▬ ▬',
    'X' : '▬ ● ● ▬',
    'Y' : '▬ ● ▬ ▬',
    'Z' : '▬ ▬ ● ●',
    '1' : '● ▬ ▬ ▬ ▬',
    '2' : '● ● ▬ ▬ ▬',
    '3' : '● ● ● ▬ ▬',
    '4' : '● ● ● ● ▬',
    '5' : '● ● ● ● ●',
    '6' : '▬ ● ● ● ●',
    '7' : '▬ ▬ ● ● ●',
    '8' : '▬ ▬ ▬ ● ●',
    '9' : '▬ ▬ ▬ ▬ ●',
    '0' : '▬ ▬ ▬ ▬ ▬'
    }


class Morse_to_English:
    """Morse to English
    decodes morse code to english/number"""
    
    def __init__(self, s):
        """User Input"""
        self.s = s
        
    def Morse_English(self):
        message = self._code_extract(self.s)
        m=''
        # # converts list to string and stroes it in m
        for i in message:
            m+=i+' '
        return m
        
    def _decode(self, s):
        for k,v in morse.items():
            if s==v:
                return k
                
    def _reform(self, s):
        s=s.replace('.','● ')
        s=s.replace('-','▬ ')
        s=s.replace('●','● ')
        s=s.replace('▬','▬ ')
        # # this removes the last unwanted space created by
        # # replace function to avoid error
        s=s[:-1]
        return s
    
    def _code_extract(self, s):
        s+='  '
        raw=''  # stores morse code  
        eng=''  # stores english or numbers
        t=[]
        for i in range(len(s)-1):
            # # checks the code
            if s[i]!=' ':
                raw+=s[i]
            # # checks if the code is of a different word
            elif s[i]==' ' and s[i+1]==' ':
                # # this is avoids translating none as morse
                # # when raw is ''
                # # which generates error
                if raw!='':
                    raw = self._reform(raw)
                    eng += self._decode(raw)
                t.append(eng)
                eng=''
                raw=''
            # # checks if the code is of the same word
            elif s[i]==' ' and s[i+1]!=' ':
                # # this is avoids translating none as morse
                # # when raw is ''
                # # which generates error
                if raw != '':
                    raw = self._reform(raw)
                    eng += self._decode(raw)
                    raw=''
        return t
    

class English_to_Morse:
    """Converts english to morse"""
    
    def __init__(self, s):
        """User Input"""
        s=s.upper()
        s+=' '
        self.s = s        
    
    def _encode(self, s):
        for k,v in morse.items():
            if s==k:
                v=v.replace(' ','')
                return v
        
    def English_Morse(self):
        """extracts each character and gives the final encoded message"""
        w = ''  # stores english
        code = ''  # stores morse
        for i in range(len(self.s)):
            if self.s[i] !=' ':
                w += self._encode(self.s[i]) + ' '
            else:
                code+= w + '  '
                w = ''
        # # omits the extra space at the end of the variable code
        return code[:-2]


import streamlit as st

"""# Welcome to the Morse-Code Translator"""

language = st.selectbox('Choose language', ['English', 'Morse Code'])

st.write(f'Translating from {language} to {"Morse Code" if language=="English" else "English"} ...')

if language == 'Morse Code':
    st.write("Example code: .... ..  -- -.--  -. .- -- .  .. ...")
    st.write("Translated: HI MY NAME IS")
    st.write("Please follow the rules for writing morse code, else the program won't work properly:")
    st.write("1. No space between codes representing a character")
    st.write('2. One Space between codes of a single word')
    st.write('3. Two Spaces between codes of different words')   

st.subheader('Text to translate')
text_to_translate = st.text_area('')

if language == 'Morse Code':
    # create object of Morse_to_English class
    obj_me = Morse_to_English(text_to_translate)
    st.subheader('Translated Text')
    # convert morse code to english
    translated_text = obj_me.Morse_English()
    st.text(translated_text)
elif language == 'English':
    # create object of English_to_Morse class
    obj_em = English_to_Morse(text_to_translate)
    st.subheader('Translated Text')
    # convert english to morse code
    translated_text = obj_em.English_Morse()
    st.text(translated_text)



    