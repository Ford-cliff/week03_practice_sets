
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("example.txt", "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")

with open("example.txt", "r") as file:
    words = file.read().split()
    print(f"Total words: {len(words)}")

with open("example.txt", "r") as file:
    content = file.read()
    print(f"Total characters: {len(content)}")
s: {len(words)}")

with open("example.txt", "r") as file:
    content = file.read()
    print(f"Total characters: {len(content)}")
