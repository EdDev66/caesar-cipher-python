import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

def run_program():
    mode = input('Type 1 to encrypt, 2 to decode: ')
    word = input('Word: ')
    shift = int(input('shift: '))
    if mode == '1':
        caesar('encrypt', word, shift)
    elif mode == '2':
        caesar('decode', word, shift)
    else:
        print('Invalid input!')


def caesar(mode, word, shift):
    shift_direction = 1
    if mode == 'decode':
        shift_direction = -1
    cipher_text = ''
    if shift > 26:
        shift = shift % 26
    for char in word:
        if char not in alphabet:
            cipher_text += char
            continue
        new_position = alphabet.index(char) + (shift * shift_direction)
        if new_position > 26:
            new_position = new_position - 26
        if new_position < 0:
            new_position = 26 + new_position
        cipher_text += alphabet[new_position]
    print(cipher_text)
        
run_program()

while True:
    continue_code = input('Type yes if you want to go again. Otherwise type no.\n')
    if continue_code == 'yes':
        run_program()
    else:
        print('Goodbye')
        break