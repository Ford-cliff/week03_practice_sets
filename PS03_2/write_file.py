with open("source.txt", "w") as file:
    file.write("Hello, World!\n")

with open("source.txt", "a") as file:
    file.write("This is appended text.\n")

with open("source.txt", "r") as source, open("destination.txt", "w") as dest:
    dest.write(source.read())
 another
with open("source.txt", "r") as source, open("destination.txt", "w") as dest:
    dest.write(source.read())
