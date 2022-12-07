palabra = input('escriba un palindromo: ')

def es_palindromo(n):
    palindromo = n[::-1]
    if palabra == palindromo:
        return "SI es un palindromo"
    else:
        return "NO es un palindromo"

print(es_palindromo(palabra))