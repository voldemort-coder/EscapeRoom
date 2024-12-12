#import string

def este_palindrom(text):
    # Eliminăm spațiile și semnele de punctuație
    text = text.lower()  # Ignorăm diferențele de litere mari și mici
    text = ''.join(c for c in text if c.isalnum())  # Păstrăm doar literele și cifrele
    return text == text[::-1]  # Verificăm dacă este identic citit invers, funcția [::-1] inversează șirul de caractere

while True:
    text = input("Introdu un text pentru a verifica dacă este palindrom: ")

    if este_palindrom(text):
        print(f"'{text}' este un palindrom :D")
    else:
        print(f"'{text}' NU este un palindrom :(")