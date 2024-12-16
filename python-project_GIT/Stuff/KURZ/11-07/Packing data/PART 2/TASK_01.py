import pickle

class Airplane:
    def __init__(self, model, capacity, range, airline):
        self.model = model  # Model of the airplane (e.g., "Boeing 737")
        self.capacity = capacity  # Passenger capacity
        self.range = range  # Maximum range in kilometers
        self.airline = airline  # Airline operating the airplane

    def display_info(self):
        print(f"Airplane Model: {self.model}")
        print(f"Capacity: {self.capacity} passengers")
        print(f"Range: {self.range} km")
        print(f"Airline: {self.airline}")

def save_airplane_to_file(airplane, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(airplane, file)
        print(f"The airplane has been successfully saved to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while saving the airplane: {e}")

def load_airplane_from_file(filename):
    try:
        with open(filename, 'rb') as file:
            airplane = pickle.load(file)
        print(f"The airplane has been successfully loaded from '{filename}'.")
        return airplane
    except Exception as e:
        print(f"An error occurred while loading the airplane: {e}")
        return None

# Example usage:
# Creating an instance of Airplane
my_airplane = Airplane("Boeing 737", 189, 5600, "Delta Airlines")

# Displaying information about the airplane
my_airplane.display_info()

# Saving the Airplane object to a file
save_airplane_to_file(my_airplane, 'airplane.pkl')

# Loading the Airplane object from the file
loaded_airplane = load_airplane_from_file('airplane.pkl')

# Displaying information about the loaded airplane, if loading was successful
if loaded_airplane:
    loaded_airplane.display_info()