words = input("Enter a character: ")
shift = 3
ces=""
for word in words:
 letter = word.lower()
 position = ord(letter) - ord('a')
 shifted_position = (position + shift) % 26
 new_letter = chr(shifted_position + ord('a'))
 if word.isupper():
    new_letter = new_letter.upper()
 ces+=new_letter

print("Encrypted character:", ces)
