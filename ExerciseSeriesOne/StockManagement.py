# Problem 1
# Stock Management

Inventory = {
    'Apple': {
        'price': 2,
        'stock': 10
    },
    'Banana': {
        'price': 1,
        'stock': 5
    },
    'Orange': {
        'price': 3,
        'stock': 8
    }
}
# menu
print('Inventory: ', Inventory)
user_orders = {}
print("Enter list of products to buy one by one: (enter 0 to exit) ")
totalCost = 0
while True:
    item = input("Product to buy: ")
    if item == '0':  # user wants to exit
        break
    if item not in Inventory:  # item is not in inventory
        print("The ordered item is currently not available in our inventory! ")
        continue
    quantity = int(input("Quantity: "))
    if int(quantity) == 0:  # user wants to exit
        break
    if Inventory[item]['stock'] < quantity:  # not enough items
        print("We currently don't have enough items as you ordered in our stock! ")
        continue
    user_orders[item] = quantity  # recording user's orders
    Inventory[item]['stock'] -= quantity  # updating Inventory
    totalCost += quantity * Inventory[item]['price']  # calculating sum of costs
print("All items are available.")
print("Your order is: ", user_orders)
print("Total cost: ", totalCost)
print("Updated Inventory: ", Inventory)
