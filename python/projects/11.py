def calculate_bill_amount(quantity, unit_price, discount, tax):
    # Calculate total amount before discount
    total_before_discount = quantity * unit_price
    
    # Calculate discount amount
    discount_amount = total_before_discount * (discount / 100)
    
    # Calculate total amount after discount
    total_after_discount = total_before_discount - discount_amount
    
    # Calculate tax amount
    tax_amount = total_after_discount * (tax / 100)
    
    # Calculate total bill amount
    total_bill_amount = total_after_discount + tax_amount
    
    return total_bill_amount

# Example usage
quantity_sold = 5
unit_price = 10
discount_percentage = 10
tax_percentage = 5

bill_amount = calculate_bill_amount(quantity_sold, unit_price, discount_percentage, tax_percentage)
print("Total bill amount:", bill_amount)
