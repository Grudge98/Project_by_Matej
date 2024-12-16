def count_vowels_and_consonants(text):
    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    num_vowels = sum(1 for char in text if char in vowels)
    num_consonants = sum(1 for char in text if char in consonants)
    return num_vowels, num_consonants

def file_statistics(input_path, output_path):
    with open(input_path, "r") as file:
        text = file.read()

    num_characters = len(text)
    num_lines = text.count("\n") + 1
    num_vowels, num_consonants = count_vowels_and_consonants(text)
    num_digits = sum(char.isdigit() for char in text)

    with open(output_path, 'w') as output_file:
        output_file.write(f"Number of characters: {num_characters}\n")
        output_file.write(f"Number of lines: {num_lines}\n")
        output_file.write(f"Number of vowels: {num_vowels}\n")
        output_file.write(f"Number of consonants: {num_consonants}\n")
        output_file.write(f"Number of digits: {num_digits}\n")


input_path = "DATA/task_2_input.txt"
output_path = "DATA/task_2_output.txt"


file_statistics(input_path, output_path)