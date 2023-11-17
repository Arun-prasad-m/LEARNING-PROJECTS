try:
    file=open("joes.txt")
    print(file.read())

except FileNotFoundError:
    print("file is not found")
else:
    print("thank you")
    file.close()