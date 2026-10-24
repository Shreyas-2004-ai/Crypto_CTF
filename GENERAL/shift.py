ciphertext = "LTWNQQF XSFHP IWFKY FRTSL"

for shift in range(26):
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            plaintext += char

    print(f"Shift {shift:2}: {plaintext}")