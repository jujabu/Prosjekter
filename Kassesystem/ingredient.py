class Ingredient:

    #Takes in the name and a set of allergies connected to the ingredient.
    def __init__(self, name):
        self._name = name
        self._diet_type = None
        self._allergy_set = set()

#Diet-type

    def update_diet_type(self, diet_type):
        self._diet_type = diet_type

    def give_diet_type(self):
        return self._diet_type

#Allergies

    #Adds an allergy
    def add_allergy(self, allergy):
        self._allergy_set.add(allergy)

    #Removes an allergy.
    #If it does not exists, the user gets informed.
    def remove_allergy(self, allergy):
        if allergy in self._allergy_set:
            self._allergy_set.remove(allergy)
        else:
            print(f"This ingredient did not have {allergy} from the beginning.")

    #Prints out all allergies.
    #If no allergies, the user gets infromed.
    def show_allergies(self):
        if self._allergy_set:
            for allergy in self._allergy_set:
                print(allergy)
        else:
            print("No allergies")
    
    #Gives the set of allergies
    def give_allergies(self):
        return self._allergy_set
    
#Magical methods
    
    #Change how an ingredient is displayed 
    def __str__(self):
        return (f"Ingredient: {self._name}\n"
    + f"Diet-type: {self._diet_type}\n"
    + f"Allergies: {self.give_allergies()}")
    
    #Lets us check if an ingredient is identical
    def __eq__(self, other):
        return self._name == other._name