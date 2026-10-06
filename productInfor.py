product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 75000,
    "quantity": 5
}

print(f"product name: ", product["name"])
print(f"product brand: ", product["brand"])

print(f"price: ", product["price"])
print(f"Qty: ", product["quantity"])

total_value = product["price"] * product["quantity"]
print("Total value: ", total_value)

product["quantity"] = product["quantity"] - 2

print("after selling: ", product["quantity"] )