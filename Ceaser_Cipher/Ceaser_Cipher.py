# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# shift = 5
# shifted_alphabet = ''

# for i in range(len(alphabet)):
#     new_index = i + shift
#     if new_index >= len(alphabet):
#         new_index = new_index - len(alphabet)
#     shifted_alphabet += alphabet[new_index]
#     # print(shifted_alphabet)

# # print(shifted_alphabet)

# translation_table = str.maketrans(alphabet, shifted_alphabet)

def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = encrypt('freeCodeCamp', 3)
print(encrypted_text)