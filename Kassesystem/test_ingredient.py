from ingredient import Ingredient

print("Makes 2 Ingredient-objects")
tomato = Ingredient("Tomato")
cream = Ingredient("Cream")

print("Updates the ingredients with their diet-type")
tomato.update_diet_type("Vegan")
cream.update_diet_type("Vegetarian")

print("Checks if it worked")
assert(tomato._diet_type == "Vegan")
assert(cream._diet_type == "Vegetarian")

print("Checks the type of diet of an ingredient")
print(tomato.give_diet_type())

print("Adds an allergy to the cream-object 2 times to show it only adds one time")
cream.add_allergy("Lactose")
cream.add_allergy("Lactose")
print(cream)
print("Checks if tomato is empty and cream contains something")
assert(not tomato._allergy_set)
assert(cream._allergy_set)

print("Shows allergies of both objects")
tomato.show_allergies()
cream.show_allergies()

print("Removes allergy from both objects")
tomato.remove_allergy("Lactose")
cream.remove_allergy("Lactose")

print("Checks if both objects have no allergies")
assert(not tomato._allergy_set)
assert(not cream._allergy_set)

print("Gives all allergies of the objects as a set")
print(tomato.give_allergies())
print(cream.give_allergies())