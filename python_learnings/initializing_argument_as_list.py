class Person:
    def __init__(self, favorite_food: list = []):
        self.favorite_food = favorite_food


sam = Person()
ash = Person()

sam.favorite_food.append("momo")

print(sam.favorite_food)
print(ash.favorite_food)

class Person:
	def __init__(self, favorite_food: list = []):
		self.favorite_food = favorite_food

sam = Person(favorite_food=["momo"])
ash = Person()


print(sam.favorite_food) # ['momo']
print(ash.favorite_food) # []

