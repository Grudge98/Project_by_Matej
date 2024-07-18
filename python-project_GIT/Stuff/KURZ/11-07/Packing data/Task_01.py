import pickle

def save_list_to_file():
    # Getting the list of integers from the user
    user_input = input("Enter a list of integers, separated by spaces: ")
    int_list = list(map(int, user_input.split()))

    try:
        # Saving the list to a file using pickle
        with open('integers_list.pkl', 'wb') as file:
            pickle.dump(int_list, file)
        print("The list has been successfully saved to 'integers_list.pkl'.")
    except Exception as e:
        # Handling exceptions
        print(f"An error occurred while saving the list: {e}")

def load_list_from_file():
    try:
        # Loading the list from the file using pickle
        with open('integers_list.pkl', 'rb') as file:
            new_list = pickle.load(file)
        print("The list has been successfully loaded from 'integers_list.pkl'.")
        print(f"The loaded list is: {new_list}")
    except Exception as e:
        # Handling exceptions
        print(f"An error occurred while loading the list: {e}")

# Save list to file
save_list_to_file()

# Load list from file
load_list_from_file()