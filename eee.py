def decrypt_Alpha(text,n):
    offset = (26-n)
    decrypt_text  = ""
    for char in text:
        try:
            ascii_code = ord(char)
            if ascii_code in range(65,91):
                if ascii_code in range(65,91-offset):
                    ascii_code += offset
                else:
                    ascii_code -= n
            elif ascii_code in range(97,123):
                if ascii_code in range(97,123-offset):
                    ascii_code += offset
                else:
                    ascii_code -= n
            else:
                pass
            decrypt_text += str(chr(ascii_code))
        except ValueError:
            print("Out of range")
    return decrypt_text

def decrypt_unicode(text,n):
    decrypt_text  = ""
    
    for char in text:
        try:
            ascii_code = ord(char)
            decrypt_text += str(chr(ascii_code+n))
        except ValueError:
            print("Out of range")
    return decrypt_text


text = str(input("input crypted text here: "))
for n in range(76):
    #print(decrypt(text,n),n)
    print(decrypt_Alpha(text,n),decrypt_unicode(text,n),n)


#cap 65-90 97-122       97->  67
#    68-93 100-125      z a b c