filename = "example.txt"

with open(filename, "r") as file:
    lines = file.readlines()
    print("File Contents:")
    for line in lines:
        print(line.strip())

    print(f"\nTotal Lines: {len(lines)}")

    words = sum(len(line.split()) for line in lines)
    print(f"Total Words: {words}")

    chars = sum(len(line) for line in lines)
    print(f"Total Characters: {chars}")
