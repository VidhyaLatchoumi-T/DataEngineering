def describe_pet(pet_name,animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Rover")

def make_pizza(size, *toppings):
    print(f"Making a {size} inch pizza with the following toppings:")
    for t in toppings:
        print(f"- {t}")

make_pizza(12,"pepperoni","mushroom","pickles")

def build_prof(first, last, **user_info):
    return {"first_name":first, "last_name":last, **user_info}

user_profile=build_prof("john","Doe",
                        location="New York", field="Engineering")
print(user_profile)