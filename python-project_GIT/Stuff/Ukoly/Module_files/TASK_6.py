def find_and_replace(input_path, search_word, replace_word):
    with open(input_path, "r") as file:
        text = file.read()

    updated_text = text.replace(search_word, replace_word)      # replaces search_word by specified_word

    with open(input_path, "w") as file:
        file.write(updated_text)

    return "Word was replaced"


input_path = "DATA/TASK_6/input.txt"
search_word = input("Enter a word you want to replace: ")
replace_word = input("Enter a replacement word: ")

result = find_and_replace(input_path, search_word, replace_word)
print(result)