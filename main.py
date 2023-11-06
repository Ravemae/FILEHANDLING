with open("newfile.txt", mode= 'w') as file:
    file.write("This file was appended")
with open("newfile.txt", mode= 'a') as file:
    file.write("This file was appended")

import os
if os.path.exists("newfile3.txt"):
    os.remove("newfile3.txt")
else:
    print("File not found")


with open("text/text2/demo.txt") as file:
    print(file.read())