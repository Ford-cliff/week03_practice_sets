old_word, new_word = "old", "new"
with open("text.txt", "r") as file:
    content = file.read()
content = content.replace(old_word, new_word)
with open("text.txt", "w") as file:
    file.write(content)
") as file:
    file.write(content)
