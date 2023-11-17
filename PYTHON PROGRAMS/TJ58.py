try:
    file=open("joes.txt")
    for line in file:
        print(line)

except FileNotFoundError:
    print("file is not found")
else:
    print("thank you")
    file.close()