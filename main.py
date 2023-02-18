import math
my_profit = []

while True:
    cost_price = float(input('cost price? '))
    if cost_price == 0:
        break
    selling_price = float(input('selling price? '))

    profit = selling_price - cost_price
    correct_profit = round(profit, 2)
    my_profit.append(correct_profit)

print(sum(my_profit))



