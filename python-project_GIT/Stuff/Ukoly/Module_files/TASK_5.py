def count_word_occurence(input_path, word):
    with open(input_path, "r") as file:
        text = file.read().lower()              # přečte soubor a změní na lower case
        word = word.lower()                     #změní slovo na lower case
        word_count = text.split().count(word)   # rozdělí text na jednotlivý slova / .count spočítá kolikrat se slovo vyskytuje
        return word_count


word = input("Enter a word you want to count: ")
input_path = "DATA/TASK_5/input.txt"
occurence_of_word = count_word_occurence(input_path, word)
print(f"The word -{word}- occures {occurence_of_word} times" )
