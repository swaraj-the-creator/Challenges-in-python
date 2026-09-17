milk = int(input("Enter packets of milk you will you buy:"))
sugar = int(input("Enter packets of sugar you will you buy:"))
wheat = int(input("Enter Kg's of wheat you will buy you will you buy:"))
honey = int(input("Enter bottles of honey you will you buy:"))
pm = 65
ps = 100
pw = 150
ph = 99
totpm = pm * milk
totps = ps * sugar
totpw = pw * wheat
totph = ph * honey
total = totpm + totph + totps + totpw
discount = 2
gratot = total / discount
print("\n===== BILL =====")
print("Wheat ",wheat,"Kg ==",totpw)
print("Milk ",milk,"packets ==",totpm)
print("Sugar ",sugar,"packets ==",totps)
print("Honey ",honey,"bottels ==",totph)
print("Discount : ",discount)
print("Total :",gratot)
print("================")
