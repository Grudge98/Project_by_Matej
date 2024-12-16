def compare_files(path1, path2):
    with open(path1, "r") as file1, open(path2, "r") as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

    mismatch_found = False
    for line1, line2 in zip(file1_lines, file2_lines):
        if line1 != line2:
            print("missmatch found")
            print(f"File 1: {line1.strip()}")
            print(f"File 2: {line2.strip()}")
            mismatch_found = True

    if not mismatch_found:
        print("Files match")


path1 = "DATA/file1.txt"
path2 = "DATA/file2.txt"
compare_files(path1,path2)