def base_rate(w):
    return 5 if w < 2 else (12 if w <= 10 else 20)

def surcharge(spd):
    if spd == "standard": return 0
    if spd == "express":  return 8
    if spd == "overnight":return 25
    raise ValueError("Speed must be standard/express/overnight.")

def shipping_cost(weight, speed, member, total, saturday):
    if weight < 0 or total < 0: raise ValueError("Weight/total must be non-negative.")
    if member not in ("yes","no"): raise ValueError("Member must be yes/no.")
    if saturday not in ("yes","no"): raise ValueError("Saturday must be yes/no.")

    cost = base_rate(weight) + surcharge(speed)
    if total > 100:                      # free standard; faster pays only the difference
        cost = surcharge(speed)
    if saturday == "yes":
        cost += 5
    if member == "yes" and cost > 0:
        cost *= 0.8                      # 20% off
    return cost

# ---- I/O + error handling ----
try:
    Weight   = input("Enter package weight (lbs): ")
    Speed    = input("Enter delivery speed (standard/express/overnight): ")
    Member   = input("Are you a premium member (yes/no): ")
    Total    = input("Enter order total ($): ")
    Saturday = input("Need Saturday delivery (yes/no): ")

    weight = float(Weight)
    speed = Speed.lower()
    member = Member.lower()
    total = float(Total)
    saturday = Saturday.lower()

    print("Shipping cost: $", shipping_cost(weight, speed, member, total, saturday))
except ValueError as e:
    print("Error:", e)



# ---------- SIMPLE NO FUNCTIONS WAY ---------- #
# Weight = input("Enter package weight (lbs):")
# Speed = input("Enter delivery speed (standard/express/overnight:")
# Member= input("Are you a premium member (yes/no):")
# Total = input("Enter order total ($):")
# Saturday = input("Need Saturday delivery (yes/no):")

# weight=float(Weight)
# speed=str(Speed).lower()
# member=str(Member).lower()
# total=float(Total)
# saturday=str(Saturday).lower()

# order = 0

# if weight < 2:
#   order = 5
# elif weight <= 10:
#   order = 12
# else:
#   order = 20

# if speed == "express":
#   order = order +8
# elif speed == "overnight":
#   order = order + 25
# elif speed == "standard":
#   order = order + 0
# else:
#   print("Invalid delivery method: Choose from the following (Standard/Express/Overnight)")

# if total > 100:
#   if speed == "standard":
#     order = 0
#   elif speed == "express":
#     order = 8
#   elif speed == "overnight":
#     order = 25

# if saturday == "yes":
#   order = order + 5

# if member == "yes":
#  order = order * 0.8

# print("Your shipping cost: $", order)
