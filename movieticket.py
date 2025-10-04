Age = input("Enter the age:")
Day = input("Enter the day of the week:")
age = int(Age)
day = str(Day).lower()

price = 0
if age < 12:
  price = 6
elif age >= 13 and age <= 22:
  price = 8
elif age >= 23 and age <= 64:
  price = 12
elif age >= 65:
  price = 7
if day == "saturday" or day == "sunday" :
  price += 3
if day == "wednesday":
  price -= 2
print("Your ticket price is:$",price)
