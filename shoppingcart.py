cart = ["apple", "milk", "bread", "apple", "eggs", "milk"]

unique_items = list(set(cart))

unique_items.append("cheese")

unique_items.remove("bread")

print("Unique items :", unique_items)

unique_items.sort()
print("alpha_o :",unique_items)

print("Length: ", len(unique_items))
