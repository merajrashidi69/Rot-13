#rot-13 cipher
letters = 'abcdefghijklmnopqrstuvwxyz'
def shift(message):
    message = message.lower()
    result = ''
    for characters in message:
        index = (letters.find(characters) + 13) % len(letters)
        result += letters[index]
    print(result)
while True:
    user = input('Enter message to encrypt or decrypt: ')
    shift(user)
            
