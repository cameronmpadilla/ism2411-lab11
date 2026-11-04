# 1: I would use the .get method in real life if I was making a form that had required questions on it, that way if someone else was filling it out then they can go back and fill out what they missed. I would use the bracket method if I was trying to find a field in a databasde. 
# 2: This pattern reminds me of how in excel you can make equations in a cell to get the certain value you need based on other cells. The Python verison is helpful for larger datasets because you will write in a lot less code and it can cover more space with less steps. 

# Exercise 1

customer = {"name": "Alice", 
            "email": "alice@example.com", 
            "tier": "gold", 
            "ytd_spend": 12400,}

print(customer['name'])
print(customer['email'])
print(customer['tier'])
print(customer['ytd_spend'])
print(customer)

# Excercise 2

customer['phone']= '813-555-0342'

print(customer)
customer['tier'] = 'platinum'

print(customer)
del customer['email']

print(customer)

# Exercise 3

print(customer.get('email', "Email not found"))

# try:
#     print(customer['email'])
# except KeyError as error:
#     print("KeyError Caught: {error}")

# Exercise 4

for key, value in customer.items():
    print(f"{key}: {value}")

for item in customer:
    print(item)

# Exercise 5

tier_discounts = {'bronze': 0, 'silver': 0.05, 'gold': 0.10, 'platinum': 0.15}

purchase = 200
discount_rate = tier_discounts.get(customer['tier'], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount rate: {discount_rate}")
print(f"Final price: {final_price}")

# Exercise 6

customers = [{'name': 'Bob', 'tier': 'silver', 'ytd_spend': 3200},
              {'name': 'Carol', 'tier': 'gold', 'ytd_spend': 8750},
              {'name': 'David', 'tier': 'bronze', 'ytd_spend': 450}]

for record in customers:
    rate = tier_discounts.get(record['tier'], 0)
    discount = 300 * rate

    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")

# Exercise 7
catalog = {"Widget A": {"price": 9.99, 'stock': 150},
           "Gadget C": {'price': 49.99, 'stock': 8}}

for product, details in catalog.items():
    if details['stock'] < 20:
        print(f"Low Stock: {product} - Only {details['stock']} left in stock")

# Exercise 8

transactions = [{'region': 'South', 'amount': 300}, {'region': 'north', 'amount': 150},
                {'region': 'East', 'amount': 200}]

sales_by_region = {}
for sale in transactions:
    region = sale['region']
    sales_by_region[region] = sales_by_region.get(region, 0) + sale['amount']
print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
    

