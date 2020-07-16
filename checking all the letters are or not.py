lower="abcdefghijklmnopqrstuvwxyz"

string=input("Enter string= ")

for ch in lower:
    if ch not in string:
        print("no,not all letters are there in the string")
        break
else:
    print("yes, all the letters are present in the string")
