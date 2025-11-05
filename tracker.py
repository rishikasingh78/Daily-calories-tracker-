# NAME - RISHIKA SINGH 
# ROLL NUMBER - 2501730405 

print("Welcome to daily calories tracker !")
print("This helps you to track your daily calories intake")

meal = []
calories = []

number_of_meal = int(input("enter the number of meal you have taken today : "))

for i in range(number_of_meal):
    print(f"meals are {i+1}")
    meal_name = input("enter the name of meal :")
    meal_calories = float(input("enter the meal calories : "))
    meal.append(meal_name)
    calories.append(meal_calories)
total_calories = sum(calories)
average_calories = total_calories/len(calories)

print("caloriers summary")
print(f"total calories intake {total_calories}")
print(f"average calories {average_calories}")

limit = float(input("enter your limits: "))
if total_calories>limit:
    print("you have exceeded your daily limits")
elif total_calories== calories:
    print("you have exactly met your daily calories limit ")
else :
    print("your are within your daily calories limits ! ")

print("Thanks for using daily calories tracker! ")
print(f"{'meal name '<15}\t{'calories'}")
print("_"*35)
for meal , cal in zip(meal , calories):
    print(f"{meal:<15}\t{cal}")

print("-" * 35)
print(f"{'Total:':<15}\t{total_calories}")
print(f"{'Average:':<15}\t{average_calories:.2f}")
print("-" * 35)