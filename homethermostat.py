Hour = input("Enter the current hour:")
Home = input("Is someone home? (yes/no)")
Out = input("Enter the outside temperature (Farenheit):")
Eco = input("Is Eco mode enabled? (yes/no)")

hour=int(Hour)
home=str(Home).lower()
out=int(Out)
eco=str(Eco).lower()
temperature = 72

if (32 >= out <= 95):  # 33 this is not true
  temperature = 72
else:  # looks for the next true statement
    if (hour >= 21 or hour <= 6):
      temperature -= 5
    elif (6 < hour <= 9):
      temperature += 2
    
    if (home == "no"):
      temperature -= 8
    
    if (eco == "yes"):
      temperature -= 3
print("Target temperature:",temperature,"F", sep="")
