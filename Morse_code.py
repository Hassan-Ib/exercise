# CODEWARS MORSE CODE TO HUMAN READABLE LANGUAGE


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


# Alphabelt_morse = {v: k for k, v in morse_alphabets.items()}
#
# print(Alphabelt_morse)


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
                if len(space) % 2 != 0:
                    code = ''
                    message = ''.join(morse_alphabets[code])
                    print(message, end='')
        else:

            print('not in morse alphabet')


morse_decoder('.... . -.--   .--- ..- -.. .   .... --- .--   .- .-. .   -.-- --- ..-')
