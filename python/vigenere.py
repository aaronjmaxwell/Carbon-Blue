def vigenere(key, msg, encode=True):
    chars = []
    for i in range(len(msg)):
        k = key[i % len(key)]
        if encode:
            c = chr(ord(msg[i]) + ord(k) % 256)
        else:
            c = chr((256 + ord(msg[i]) - ord(k)) % 256)
        chars.append(c)
    return "".join(chars)
