from collections import Counter

with open("text.txt", "r") as file:
    words = file.read().split()
word_counts = Counter(words)
with open("word_frequencies.txt", "w") as output:
    for word, count in word_counts.items():
        output.write(f"{word}: {count}\n")
ems():
        output.write(f"{word}: {count}\n")
