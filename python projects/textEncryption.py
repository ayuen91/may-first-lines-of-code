import random
import string

text = input("Enter the text you want to encrypt: ")
key = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
"".join(key)
random.shuffle(key)
encrypted_text = ''

def text_encryptor(text):
    global encrypted_text
    global key
    for i in text:
        encrypted_text += key[text.index(i)]
    return encrypted_text

print(text_encryptor(text))

    