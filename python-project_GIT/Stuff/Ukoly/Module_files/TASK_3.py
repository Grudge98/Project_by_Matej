def delete_last_line(input_path, output_path):
    with open(input_path, "r") as file:             # open file (r = read)
        lines = file.readlines()                    # used to read file  > saveds it to lines

        lines = lines[:-1]                          # removes the last line

    with open(output_path, "w") as file:            # open file (w = write)
        file.writelines(lines)                      # writes the last line to the output


input_path = "DATA/TASK_3/input.txt"
output_path = "DATA/TASK_3/output.txt"

delete_last_line(input_path, output_path)
