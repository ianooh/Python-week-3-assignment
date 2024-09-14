def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * discount_percent/100
        final_price = price - discount
        return final_price
    else:
        return price
    
price = float(input("Enter your price: " ))
discount_percent = float(input("What is your discount percentage? "))
print("This is your final price ", calculate_discount(price, discount_percent))