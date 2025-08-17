def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
    else:
        final_price = price
    return final_price

try:
    price = float(input('Please enter the price of the item: '))
    discount_percent = float(input('Please enter the discount percent applied on the item: '))
    final_price = calculate_discount(price, discount_percent)
    print(f"The final price after discount is: {final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numerical values for price and discount.")
