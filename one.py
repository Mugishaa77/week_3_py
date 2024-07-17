"""
Create a function named calculate_discount(price, discount_percent) that calculates the final price 
after applying a discount. The function should take the original price (price) and the discount
 percentage (discount_percent) as parameters. 
If the discount is 20% or higher, apply the discount; otherwise, return the original price.
"""

def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract the discount amount from the original price
        final_price = price - discount_amount
    else:
        # If the discount is less than 20%, return the original price
        final_price = price
    
    return final_price


"""
Using the calculate_discount function, prompt the user to enter the original price of an item and 
the discount percentage. Print the final price after applying the discount, or if no discount was 
applied, print the original price.

"""
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        final_price = price
    return final_price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
if discount_percent >= 20:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {original_price}")
