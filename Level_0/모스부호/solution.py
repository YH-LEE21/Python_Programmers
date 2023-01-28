def morseTranslation(letter):
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    return "".join(morse[i] for i in letter.split())

print(morseTranslation(".... . .-.. .-.. ---"))#hello
print(morseTranslation(".--. -.-- - .... --- -."))#python