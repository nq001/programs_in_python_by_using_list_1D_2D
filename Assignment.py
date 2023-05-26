
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Read list of items, quantities, and unit price then print all items and 
# related data in tabular form along with invoice total.

lis,lis2,lis3 = [],[],[]
total = 0 
to = 0 # to keep sum value
for i in range(3):

    name = input("enter type of item: ")
    qty = float(input("enter the quantities: "))
    unit_p = float(input("enter unti price: "))

    lis.append(name)
    lis2.append(qty)
    lis3.append(unit_p)

    total = unit_p * qty 
    to = to + total

print("item\t\tqty\t\tunit_price")
print("-"*40)

a = 0
for x in lis[:]:
    print(f"{lis[a]}\t\t{lis2[a]}\t\t{lis3[a]} $ ")
    a += 1

print("-"*40)
print(f"the total: {to}$")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



