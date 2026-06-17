## RENT CALCULATOR

## Input:
# Rent of Flat/Room
# Food Expenses
# Electricty Units Consumed
# Electricity Cost per Unit
# Number Of Flat/room mates

## Output:
# Total Amount You Have To Pay

rent = int(input("Enter The Rent of Flat: "))
food_expenses = int(input("Enter the Food Expenses: "))
electricity_units = int(input("Enter The Electricity units consumed"))
electricity_cost_per_unit = int(input("Enter the Cost Per Unit Of Electricity: "))

electricity_bill = electricity_units * electricity_cost_per_unit

total_amount = rent + food_expenses + electricity_bill

total_number_of_roommates = int(input("Enter the Number of Flat mates: "))

amount_per_person = total_amount / total_number_of_roommates

print("Total Amount To Be Paid Individually: ", amount_per_person)