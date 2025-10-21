class Ingredient:

    def __init__(self, name):
        self._name = name
        self._allergy_set = {}

    def add_allergy(self, allergy):
        self._allergy_set.add(allergy)

    def show_allergy(self):
        for allergy in self._allergy_set:
            print(allergy)

    def give_name(self):
        return self._name
    
    def give_allergy_set(self):
        return self._allergy_set