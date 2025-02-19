#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Unknown", breed="Beagle"):
        self._name = "Unknown"  # Initialize private attributes first
        self._breed = "Beagle"  

        self.name = name  # Now use property setters
        self.breed = breed  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            if self._breed in APPROVED_BREEDS:  # Ensures it prints only once
                print("Breed must be in list of approved breeds.")
            self._breed = "Unknown"

# Testing
if __name__ == "__main__":
    dog1 = Dog("Buddy", "Pug")
    print(f"Dog's name: {dog1.name}, Breed: {dog1.breed}")

    dog2 = Dog("Max", "Wolf")  # Invalid breed (prints once)
    dog2.breed = "Wolf"  # Should NOT print again

   