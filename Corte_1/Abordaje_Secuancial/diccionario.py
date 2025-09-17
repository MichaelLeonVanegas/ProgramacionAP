# #### Get A Key
# #you can access the values in it by providing the key:

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

pedido_Altura = input("¿Que edifiio quiere conocer su altura? ")
# print(building_heights[pedido_Altura])

if pedido_Altura in building_heights:
  print(building_heights[pedido_Altura])

building_heights.get(pedido_Altura)

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

pedido_Zodiaco = input("¿Que elemento quiere saber sus zodiacos? ")
# print(zodiac_elements[pedido_Zodiaco])

if pedido_Zodiaco in zodiac_elements:
    print(zodiac_elements[pedido_Zodiaco])
    
zodiac_elements.get(pedido_Zodiaco)

# ###
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
pedido_Id = input("Ingrese el nombre que quiere su id ")
user_ids.get(pedido_Id)
if user_ids.get(pedido_Id) == None:
    tc_id = 1000
else:
    tc_id = user_ids.get(pedido_Id)
print(tc_id)
    
# ###Delete a Key
#.pop() works to delete items from a dictionary, when you know the key value.

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(320291, "No Prize"))
## Prints "Gift Basket"


#print(raffle)
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
# print(raffle.pop(100000, "No Prize"))
# # Prints "No Prize"
# print(raffle)
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
# print(raffle.pop(872921, "No Prize"))
# # Prints "Concert Tickets"
# print(raffle)
# # Prints {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

# ##Get All Keys
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(test_scores))
# # Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]

for student in test_scores.keys():
  print(student)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)

##Get All Values
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

for score_list in test_scores.values():
  print(score_list)
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for exercises in num_exercises.values():
  total_exercises += exercises
print(total_exercises)

##Get All Items
# biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

# for company, value in biggest_brands.items():
#  print(company + " has a value of " + str(value) + " billion dollars. ")

# pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

# for occupation, percentage in pct_women_in_occupation.items():
#   print("Women make up " + str(percentage) + " percent of " + occupation + "s.") 
