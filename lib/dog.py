# lib/dog.py

class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei",
        "Beagle", "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="Doggo", breed="Pug"):
        self._name = None
        self._breed = None

        # Only print name message if user actually passed a name
        if name != "Doggo":
            self.name = name
        else:
            self._name = name  # Set directly without print

        # Only set breed if name is valid
        if self._name is not None:
            self.breed = breed

    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print(f"Setting name to {name}.")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        print("Retrieving breed.")
        return self._breed

    def set_breed(self, breed):
        if breed in Dog.approved_breeds:
            print(f"Setting breed to {breed}.")
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
