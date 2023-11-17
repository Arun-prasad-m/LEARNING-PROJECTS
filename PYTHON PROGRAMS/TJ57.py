try:
    file=open("joes.txt")
    print(file.readlines())
    print(file.readline(2))

except FileNotFoundError:
    print("file is not found")
else:
    print("thank you")
    file.close()