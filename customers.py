#



print("--- Excercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend" : 12400,
}

print(customer["name"])  # Output: Alice
print(customer["email"])  # Output:
print(customer["tier"])  # Output: gold
print(customer["ytd_spend"])  # Output: 12400



print("--- Excercise 2 ---")
customer['phone'] = '555-5555' #adding a new key-value pair to the dictionary
print(customer)  # Output: {'name': 'Alice', 'email': '
customer['tier'] = 'platinum' #updating the value of an existing key in the dictionary
print(customer)  # Output: {'name': 'Alice', 'email': 'alice@example
del customer['name'] #removing a key-value pair from the dictionary
print(customer)  # Output: {'email': 'alice@example.com', 'tier': 'platinum', 'ytd_spend': 12400, 'phone': '555-5555'}

print(customer.get('ytd_spend', 'NaN'))

print("--- Excercise 3 ---")
print(customer.get("email", "no email on file"))

#try:
   #print(customer["email"])
#except KeyError:
    #print("KeyError caught: ", error)
print("--- Excercise 4 ---")  
for key in customer:
    print(key, ":", customer[key])
for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])


print("--- Excercise 5 ---")

tier_discounts = {
    "bronze": 0, 
    "silver": 0.05, 
    "gold": 0.10,
    "platinum": 0.15
}

purchase = 200

discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")



print("--- Excercise 6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},  
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discounted_price = 200 * rate
    print(f"Customer: {record['name']}, Tier: {record['tier']}, Discounted Price: ${discounted_price:.2f}")


print("--- Excercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - Only {product_details['stock']} left")



print("--- Excercise 8 ---")
transactions = [
    {"Region": "South", "amount": 300},
    {"Region": "North", "amount": 150},
    {"Region": "South", "amount": 200},
]

sales_by_region = {}
for sales in transactions:
    region = sales["Region"]
    amount = sales["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region) 

for region in sorted(sales_by_region): 
    print(f"{region}: {sales_by_region[region]:.2f}")  # Output: {'South': 500, 'North': 150}