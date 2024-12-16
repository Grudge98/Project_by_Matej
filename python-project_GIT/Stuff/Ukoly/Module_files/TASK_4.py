def find_longest_line(input_path):
    max_length = 0

    with open(input_path, "r") as file:
        for line in file:                               # reads line by line
            max_length = max(max_length, len(line))     # updates the line to the longest

    return max_length


input_path = "DATA/TASK_4/input.txt"
longest_line = find_longest_line(input_path)
print(f"The length of the longest line is > {longest_line} < symbols")

