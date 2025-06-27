customers = [
    ('mary', 'cold mango juice'),
    ('maurn', 'tea'),
    ('steve', 'lemonade'),
    ('pearl', 'lemongrass tea'),
    ('ken', 'chai latte'),
    ('jemoh', 'mocha cappuccino'),
    ('clarris', 'Americano,heavy cream'),
    ('lerry', 'coffee,less sugar')
]
for customer, drink in customers:
    print(f"making{drink}...")
    print(f"order for {customers}!")
for _, drink in sorted(customers,key=lambda x: x[1]):
    print(f"{drink}")
     
