inventory = {
    "apple": 20,
    "banana": 15,
    "mango": 10,
    "orange": 8
}

item = input("Enter a item name: ")

if item in inventory:
    sold = int(input("How many items were sold?"))

    inventory[item] = inventory[item] - sold

    if inventory[item] == 0:
        del inventory[item]
    else:
        print("Item doesnot exist")
print("update inventory: ", inventory[item])

for item in inventory:
    print(item ,":", inventory[item])

