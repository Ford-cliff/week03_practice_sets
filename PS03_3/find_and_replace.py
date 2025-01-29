filename = "example.txt"
old_word = "old"
new_word = "new"

with open(filename, "r") as file:
    content = file.read().replace(old_word, new_word)

with open(filename, "w") as file:
    file.write(content)
