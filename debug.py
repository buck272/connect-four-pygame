def order_pizza(size, *toppings, **details):
    print(f"Ordered a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    
    print("\nDetails of the order are:")
    for key, value in details.items():
        print(f"- {key}: {value}")

key, value = (1, 2)

my_dict = {"delivery": True, "tip": 5}

print(my_dict.items())