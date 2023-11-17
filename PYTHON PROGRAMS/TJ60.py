import os
 
if os.path.exists("joes.txt"):
    os.remove("joes.txt")
else:
    print("File Not Found")