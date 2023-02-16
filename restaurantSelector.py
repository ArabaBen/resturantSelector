#Araba Ocran, UA ID:  001495953, INF308


# Define a dictionary of restaurants with a list of their available optionse
restaurants = {
    'Bee Natural': ['keto', 'vegetarian', 'vegan', 'gluten-free'],
    'Panera Bread': ['keto', 'vegetarian', 'gluten-free'],
    'Tricky Thai': ['vegetarian'],
    'Kazan Ramen': ['keto', 'vegetarian', 'vegan'],
}
#introduction promt just for fun
print("Hi Welcome to Corprate Caters. We are here to help you pick a restaurant! Let's get started")

orderName = input("Please enter Your Name:")
print("Hi," + orderName)
print("help me help you select a resturant for your team and committee!")


#user input for diet/ food restriction quetions:
    
#isketo = input("Does your committee have anyone on a keto diet?")
#isVegetraian = input("Does your committee have any vegetarians?")
#isVegan =input("Does your committee have any vegans?")
#isGlutenFree =input("Does your committee have anyone on a gluten-free diet?")
#if diet = input
# Prompt for the users input for diet/ food restriction quetions: if yes then... =.. BUT if no then ...=... 

dietRestrictions = []
if input("Does your committee have anyone on keto diet? ").lower() == "yes":
    dietRestrictions.append("keto")
if input("Does your committee have any vegetarians? ").lower() == "yes":
    dietRestrictions.append("vegetarian")
if input("Does your committee have any vegans? ").lower() == "yes":
    dietRestrictions.append("vegan")
if input("Does your committee contain people that are gluten-free? ").lower() == "yes":
    dietRestrictions.append("gluten-free")

# Using for, in , and if statement to gathher the arry or list of satisfying resturants 
goodRestaurants = []
for restaurant, options in restaurants.items():
    if all(option in options for option in dietRestrictions):
        goodRestaurants.append(restaurant)

# finally this section will print out the list of satisfying restaurants as output for the user using if, else statement 
if len(goodRestaurants) == 0:
    print("Sorry, no restaurant was found that can satisfy everyone's restrictions. Try a build your own salad bar.")
else:
    print("Great news" + orderName + "!!" + " The following restaurant(s) can satisfy everyone's restrictions:")
    for restaurant in goodRestaurants:
        print("- " + restaurant)
         
        
