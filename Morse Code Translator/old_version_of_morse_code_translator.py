"""
***SPECIAL PROJECTS***

MORSE CODE TRANSLATOR
Now also includes:
1. speech-to-text feature
2. morse code sound feature

creator - Aryaman Bansal
"""


# # Morse Code
# # A short pulse is called a “dot” and a long pulse is called a “dash”.
# # Encoding = English to electric pulses
# # Decoding = electric pulses to English

morse ={
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



# # Morse to English
# # decodes morse code to english/number
def decode(s):
    for k,v in morse.items():
        if s==v:
            return k
            
def reform(s):
    s=s.replace('.','● ')
    s=s.replace('-','▬ ')
    s=s.replace('●','● ')
    s=s.replace('▬','▬ ')
    # # this removes the last unwanted space created by
    # # replace function to avoid error
    s=s[:-1]
    return s

def code_extract(s):
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
                raw=reform(raw)
                eng+=decode(raw)
            t.append(eng)
            eng=''
            raw=''
        # # checks if the code is of the same word
        elif s[i]==' ' and s[i+1]!=' ':
            # # this is avoids translating none as morse
            # # when raw is ''
            # # which generates error
            if raw!='':
                raw=reform(raw)
                eng+=decode(raw)
                raw=''
    return t
            
# User input
def Morse_English():
    s=input('Example code: .... ..  -- -.--  -. .- -- .  .. ...\n'
            +'Decoded: HI MY NAME IS\n'
            +'No space between codes representing a character\n'
            +'1 space between codes of a single word\n'
            +'2 spaces between codes of different words\n'
            +'Enter: ')
    
    print(s+'\n')
    message=code_extract(s)
    m=''
    # # converts list to string and stroes it in m
    for i in message:
        m+=i+' '
    return m
    
    
# # English to Morse

# # converts english to morse
def encode(s):
    for k,v in morse.items():
        if s==k:
            v=v.replace(' ','')
            return v
    
# # extracts each character and gives the final encoded message
def English_Morse():
    s = input("Enter Plain text: ")
    s=s.upper()
    s+=' ' 
    w=''  # stores english
    code=''  # stores morse
    for i in range(len(s)):
        if s[i] !=' ':
            w+=encode(s[i])+' '
        else:
            code+=w+'  '
            w=''
    # # omits the extra space at the end of the variable code
    return code[:-2]


"""
In order to play music/audio files in pygame, pygame.mixer is used 
(a pygame module for loading and playing sounds). This module contains 
classes for loading Sound objects and controlling playback. There are 
basically 4 steps in order to do so:
1. Starting the mixer
2. Loading the song
3. Setting the volume
4. Start playing the song
"""


def morse_sound(msg):
    """Plays the morse code (dot-dash) sound for the input message"""
    from pygame import mixer
    import time
    for i in msg:
        if i!=' ':
            # wait for 0.25 seconds
            time.sleep(0.25)
        else:
            # wait for 0.2 seconds
            time.sleep(0.2)
        if i=='●':
            # Starting the mixer
            mixer.init()
            # Loading the song
            mixer.music.load('morse_dot.wav')
            # Setting the volume
            mixer.music.set_volume(0.7)
            # Start playing the song
            mixer.music.play()
        elif i=='▬':
            # Starting the mixer
            mixer.init()
            # Loading the song
            mixer.music.load('morse_dash.wav')
            # Setting the volume
            mixer.music.set_volume(0.7)
            # Start playing the song
            mixer.music.play()
    pass


def english_sound(msg):
    """Plays the text in English"""
    from gtts import gTTS
    import os
    
    myText = msg
    if myText == '':
        myText='R yea man Bansal is a genius!'
        # Aryaman is pronounced as R-yea-man
    language = 'en-us'
    
    output = gTTS(text=myText, lang=language, slow=False, tld='com')
    output.save("sample.mp3")

    os.system("start sample.mp3")
    

# # User interface
s=input("1 for Morse to English\n2 for English to Morse"
        +'\n0 to quit\nEnter: ')
s=int(s)
if s==0 or s==1 or s==2:
    while s!=0:
        if s==1:
            me=Morse_English()
            print("Plain text: ",me)
            response = input('Do you want the sound?[Y/N]: ')
            if response.lower() == 'y':
                english_sound(me)
        elif s==2:
            em=English_Morse()
            print("Morse code: ",em)
            response = input('Do you want the sound?[Y/N]: ')
            if response.lower() == 'y':
                morse_sound(em)
        s=input("Enter: ")
        s=int(s)
else:
    print("Kindly enter correct number...")


# s = ''
# s=s.replace('▬', '-')
# s=s.replace('●', '.')
# print(s)


# from gtts import gTTS
# import os
# tts_en = gTTS('hello', lang='en', tld='com')
# tts_en.save("sample.mp3")
# os.system("start sample.mp3")

# tts_fr = gTTS('bonjour', lang='fr')
# tts_fr.save("sample.mp3")
# os.system("start sample.mp3")

# tts_hi = gTTS('namaste', lang='hi')
# tts_hi.save("sample.mp3")
# os.system("start sample.mp3")
