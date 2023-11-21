class Food:
    def __init__(self):
        pass
    def eating(self):
        return f'Food is anything you can eat'
    
class Carbohydrates(Food):
    def energy_giving_foods(self):
        return f'Carbohydrates include: Rice, fufu, garri, yam'
    
class Protein(Food):
    def body_building_foods(self):
        return f'Beans, Egg, Fish, Meat'
    def energy(self):
        print('It gives energy')
    
class Vitamins(Food):
    def cell_growth(self):
        return f'Citrus, Mango, Spinach, Banana, '

class Minerals(Food):
    def body_water_bal():
        return f'Iodine, Calcium, Floride, Magnesium, Zinc, Sodium'
    
class FatOil(Food):
    def fats_and_oil(self):
        return f'Olive oil, Sunflower oil, Almond oil, Vegetable fat'

class Water(Food):
    def hydration(self):
        return f'Alkaline water, Salt water, Fresh water'



chaw = Carbohydrates()
print(chaw.eating())
print(chaw.energy_giving_foods())