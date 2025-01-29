from collections import Counter

filename = "example.txt"
output_file = "word_count.txt"

with open(filename, "r") as file:
    words = file.read().split()

counts = Counter(words)

with open(output_file, "w") as out:
    for word, count in counts.items():
        out.write(f"{word}: {count}\n")
