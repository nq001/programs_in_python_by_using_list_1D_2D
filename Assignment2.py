# Super market involving using single 2-D array.

liss = [['milk','sugar','tea','water'],[4,2,8,3],[2500,4500,500,400]]

print("item\t\tqty\t\tunit_price")
print('-'*40)

for i in range(1):
    print(f"{liss[0][0]}\t\t{liss[1][0]}\t\t{liss[2][0]}")
    print(f"{liss[0][1]}\t\t{liss[1][1]}\t\t{liss[2][1]}")
    print(f"{liss[0][2]}\t\t{liss[1][2]}\t\t{liss[2][2]}")
    print(f"{liss[0][3]}\t\t{liss[1][3]}\t\t{liss[2][3]}")

t = 0
x = 0
for k in liss[1] and liss[2]:
    total = liss[1][t] * liss[2][t]
    x += total
    t += 1
    
print('-'*40)
print(f"Total = {x} ")