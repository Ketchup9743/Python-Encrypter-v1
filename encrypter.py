import time

print("##################################################################")
print("#                      Python Encrypter v1                       #")
print("##################################################################")
encrypt_request = input("Please Type what you would like encrypted")
encrypted_request = ""
for letter in encrypt_request:
    
    # Lowercase
    
    if letter == "a":
        new_letter = "Q"
    elif letter == "b":
        new_letter = "W"
    elif letter == "c":
        new_letter = "E"
    elif letter == "d":
        new_letter = "R"
    elif letter == "e":
        new_letter = "T"
    elif letter == "f":
        new_letter = "Y"
    elif letter == "g":
        new_letter = "U"
    elif letter == "h":
        new_letter = "I"
    elif letter == "i":
        new_letter = "O"
    elif letter == "j":
        new_letter = "P"
    elif letter == "k":
        new_letter = "A"
    elif letter == "l":
        new_letter = "S"
    elif letter == "m":
        new_letter = "D"
    elif letter == "n":
        new_letter = "F"
    elif letter == "o":
        new_letter = "G"
    elif letter == "p":
        new_letter = "H"
    elif letter == "q":
        new_letter = "J"
    elif letter == "r":
        new_letter = "K"
    elif letter == "s":
        new_letter = "L"
    elif letter == "t":
        new_letter = "Z"
    elif letter == "u":
        new_letter = "X"
    elif letter == "v":
        new_letter = "C"
    elif letter == "w":
        new_letter = "V"
    elif letter == "x":
        new_letter = "B"
    elif letter == "y":
        new_letter = "N"
    elif letter == "z":
        new_letter = "M"
        
    # Uppercase

    elif letter == "A":
        new_letter = "q"
    elif letter == "B":
        new_letter = "w"
    elif letter == "C":
        new_letter = "e"
    elif letter == "D":
        new_letter = "r"
    elif letter == "E":
        new_letter = "t"
    elif letter == "F":
        new_letter = "y"
    elif letter == "G":
        new_letter = "u"
    elif letter == "H":
        new_letter = "i"
    elif letter == "I":
        new_letter = "o"
    elif letter == "J":
        new_letter = "p"
    elif letter == "K":
        new_letter = "a"
    elif letter == "L":
        new_letter = "s"
    elif letter == "M":
        new_letter = "d"
    elif letter == "N":
        new_letter = "f"
    elif letter == "O":
        new_letter = "g"
    elif letter == "P":
        new_letter = "h"
    elif letter == "Q":
        new_letter = "j"
    elif letter == "R":
        new_letter = "k"
    elif letter == "S":
        new_letter = "l"
    elif letter == "T":
        new_letter = "z"
    elif letter == "U":
        new_letter = "x"
    elif letter == "V":
        new_letter = "c"
    elif letter == "W":
        new_letter = "v"
    elif letter == "X":
        new_letter = "b"
    elif letter == "Y":
        new_letter = "n"
    elif letter == "Z":
        new_letter = "m"
    elif letter == " ":
        new_letter = " "
    elif letter == "0":
        new_letter = "9"
    elif letter == "1":
        new_letter = "4"
    elif letter == "2":
        new_letter = "0"
    elif letter == "3":
        new_letter = "2"
    elif letter == "4":
        new_letter = "7"
    elif letter == "5":
        new_letter = "1"
    elif letter == "6":
        new_letter = "8"
    elif letter == "7":
        new_letter = "3"
    elif letter == "8":
        new_letter = "5"
    elif letter == "9":
        new_letter = "6"
    else:
        new_letter = letter
    encrypted_request = encrypted_request + new_letter
print("Encrypting Message....")
time.sleep(2)
print("Message Encrypted!")
print(encrypted_request)
print("Answer with Yes or No")
save_request = input("Would you like to save your encrypted text as a file?")
if save_request == "Yes":
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_request)
    time.sleep(1)
    print("File Encrypted!")
elif save_request == "No":
    print("Ok! Re-Run the application to encrypt a new message!")