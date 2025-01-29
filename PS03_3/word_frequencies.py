filename = "example.txt"
output_file = "word_count.txt"

with open(filename, "r") as file:
    words = file.read().split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

with open(output_file, "w") as out:
    for word, count in word_counts.items():
        out.write(f"{word}: {count}\n")
