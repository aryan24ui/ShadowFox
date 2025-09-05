'''You and your partner are planning a trip, and you want to track expenses.
Create two dictionaries, one for your expenses and one for your partner's
expenses. Each dictionary should contain at least 5 expense categories and their
corresponding amounts.
For example:
Your expenses
your_expenses = {"Hotel": 1200,"Food": 800,"Transportation": 500,"Attractions": 300,"Miscellaneous": 200}
Your partner's expenses
partner_expenses = {"Hotel": 1000,"Food": 900,"Transportation": 600,"Attractions": 400,"Miscellaneous": 150}
Calculate the total expenses for each of you and print the results.
Determine who spent more money overall and print the result.
Find out the expense category where there is a significant difference in spending
between you and your partner.
Print the category and the difference.'''


your_expenses = { "Hotel": 1200, "Food": 800, "Transportation": 500, "Attractions": 300, "Miscellaneous": 20 }

partner_expenses = { "Hotel": 1000, "Food": 900, "Transportation": 600, "Attractions": 400, "Miscellaneous": 15 }

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print(f"Your total expenses: {your_total}")
print(f"Partner's total expenses: {partner_total}")

# Determine who spent more
if your_total > partner_total:
    print("You spent more overall.")
elif partner_total > your_total:
    print("Your partner spent more overall.")
else:
    print("Both spent the same amount.")

# Find category with largest difference
max_diff_category = None
max_diff_amount = 0

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff_amount:
        max_diff_amount = diff
        max_diff_category = category

print(f"Largest difference is in '{max_diff_category}' with a difference of {max_diff_amount}.")
