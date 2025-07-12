def caesar_decrypt(cipher, shift):
    result = ""
    for char in cipher:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            result += char
    return result

print(caesar_decrypt("Ymnx nx f xjsyjshj dtz yfxp hnumjw tk ymj wznhp.", 5))
