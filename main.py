print("WELCOME TO PLEASURE PARKKKK!!!!!!!")

print("The gate fee is 2000 naira only")

print("Age 0 - 10 years has 80% discount")
print("Age 11 - 17 years has 60% discount")
print("Age 18 - 30 years has 40% discount")
print("Age 31 - 60 years has 20% discount")
print("Age 61 - 65 years has 10% discount")
print("Age 66 - above years has 100% discount")
gate_fee = 2000

per_discount_80 = 80
per_discount_60 = 60
per_discount_40 = 40
per_discount_20 = 20
per_discount_10 = 10
per_discount_100 = 100
N = "naira"


# discount ammount
discount_80 = per_discount_80/100 * gate_fee
discount_60 = per_discount_60/100 * gate_fee
discount_40 = per_discount_40/100 * gate_fee
discount_20 = per_discount_20/100 * gate_fee
discount_10 = per_discount_10/100 * gate_fee
discount_100 = 0
#ammount to be paid
ammount_80 = gate_fee - discount_80
ammount_60 = gate_fee - discount_60
ammount_40 = gate_fee - discount_40
ammount_20 = gate_fee - discount_20
ammount_10 = gate_fee - discount_10
ammount_100 = 0
#age conditions
age = float(input("Enter age: "))
if age <= 10:
  print(f"you have a discount of {per_discount_80} percent, so your gate fee is {ammount_80} naira {N}")
elif age >= 11 and age <= 17:
  print(f"You have a discount of { per_discount_60} percent, so your gate fee is {ammount_60} {N}")
elif age >= 18 and age <= 30:
   print(f"You have a discount of {per_discount_40} percent, so your gate fee is {ammount_40} {N}")
elif age >= 31 and age <= 60:
   print(f"You have a discount of {per_discount_20} percent, so your gate fee is {ammount_20} {N}")
elif age >= 61 and age <= 65:
   print(f"You have a discount of {per_discount_10} percent, so your gate fee is {ammount_10} {N}")
elif age >= 66:
   print(f"You have a discount of {per_discount_100} percent, so your gate fee is {ammount_100} {N}")
else:
  print(" please you are supposed to be with your creator.")
  
