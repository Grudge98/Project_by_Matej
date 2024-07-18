from dataclasses import dataclass

@dataclass
class Restaurant:
    name: str
    specialization: str
    address: str
    website: str
    phone_number: str

# Example usage
restaurant = Restaurant(
    name="Gourmet Paradise",
    specialization="French",
    address="123 Culinary St, Foodie City, FC 12345",
    website="http://gourmetparadise.com",
    phone_number="(123) 456-7890"
)

print(restaurant)