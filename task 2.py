# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")

# Number of different stocks
n = int(input("Enter number of stocks: "))

# Take user input
for i in range(n):
    stock_name = input("Enter stock symbol (e.g. AAPL): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        portfolio[stock_name] = quantity

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Stock added successfully!")
        print("Investment:", investment)
    else:
        print("Stock not available in our list.")

# Display portfolio
print("\n===== Portfolio Summary =====")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity

    print(
        stock,
        "| Quantity:", quantity,
        "| Price: $", price,
        "| Value: $", value
    )

print("\nTotal Investment Value: $", total_investment)

# Optional: Save result to a text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("===== Stock Portfolio Tracker =====\n\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity

            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: ${price} | Value: ${value}\n"
            )

        file.write(f"\nTotal Investment Value: ${total_investment}")

    print("Portfolio saved successfully in portfolio.txt")

print("\nProgram completed!")