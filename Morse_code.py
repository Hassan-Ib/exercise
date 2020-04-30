# CODEWARS MORSE CODE TO HUMAN READABLE LANGUAGE
# morse codes are writing in DOTS '.' and DASHES '-'
# the spacings btw each LETTERS of a word are one and the spacing btw WORDS are three(3)
issue: # while interpreting any space before or after the message should be ignored 


morse_alphabets = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                   '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                   '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                   '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                   '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                   '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                   '-.--': 'Y', '--..': 'Z', '': ' ', '...---...': 'SOS',
                   '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                   '.....': '5', '-....': '6', '--...': '7', '---..': '8',
                   '----.': '9', '-----': '0'}


Alphabelt_morse = {v: k for k, v in morse_alphabets.items()}    #inverse of the morse dictionary for morse code to human

print(Alphabelt_morse)


def morse_decoder(morse_codes):
    morse_codes = morse_codes.split(' ')       # to split the morse input to units
    morse_codes.insert(0, '')
    morse_codes.append('')
    space = []
    for code in morse_codes:                   # looping through the units
        if code in morse_alphabets:            # checking if each unit is the morse_alphabets dict
            if code != '':
                message = ''.join(morse_alphabets[code])
                print(message, end='')
            elif code == '':
                space.append(code)
                if len(space) == 1:
                  continue
                elif len(space) % 2 != 0:
                    code = ''
                    message = ''.join(morse_alphabets[code])
                    print(message, end='')
        else:

            print('not in morse alphabet')


morse_decoder('.... . -.--   .--- ..- -.. .   .... --- .--   .- .-. .   -.-- --- ..-')


# found a better way
# strip method did the while loop work

def morse_decoder(morse_codes):
    morse_codes = morse_codes.strip().split('  ')   # to split the morse input to units
    message = []
    for words in morse_codes:
        for letters in words.split(' '):
            message.append(morse_alphabets[letters])
    answer = ''.join(message)
    return answer
  
  
  morse_decoder('.... . -.--   .--- ..- -.. .   .... --- .--   .- .-. .   -.-- --- ..-')


