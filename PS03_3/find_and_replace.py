file1 = "file1.txt"
file2 = "file2.txt"
output_file = "merged_output.txt"

with open(file1, "r") as f1, open(file2, "r") as f2, open(output_file, "w") as out:
    out.write(f1.read() + "\n" + f2.read())
