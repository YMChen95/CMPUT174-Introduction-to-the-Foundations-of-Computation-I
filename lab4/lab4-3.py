print("begin with a vowel")
animals = ["ostrich", "antelope", "bear", "monkey", "otter", "snake", "iguana", "tiger", "eagle"]
for animal in animals:
         if animal[0] in ["a","e","i","o","u"]:
                  print(animal)
print("more than 5 letters")
for animal in animals:
         if len(animal)>5:
                  print(animal)


