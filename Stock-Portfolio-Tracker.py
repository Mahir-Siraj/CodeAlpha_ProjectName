# We define a dictionary named as  stock_prices that contains stock symbols as keys and their prices as values.
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 120,
    "MSFT": 330
}

# Dictionary to store the user's portfolio
portfolio = {}
# Keys will be stock symbols.
# Values will be how many shares the user owns of that stock.


# Welcome message
print("📈 Welcome to the Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
# Displays the available stock symbols using stock_prices.keys().

# Take user input for portfolio
while True: # A while True loop runs infinitely until the user types 'done'.
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE": # if user enter done so loop end
        break
    if stock not in stock_prices:
        print("⚠️ Stock not found. Please choose from the listed symbols.")
        continue 
    # Validates whether the entered stock symbol exists in our stock_prices dictionary.
	# If not, the user is warned and the loop restarts with continue.

    try: 
        quantity = int(input(f"Enter quantity of shares for {stock}: ")) # It takes quantity of shares user buys
        if quantity < 0: # if quanity is negative so it raise an error
            raise ValueError
        portfolio[stock] = portfolio.get(stock,0) + quantity # Adds the quantity to the portfolio dictionary.
# portfolio.get(stock, 0) ensures that if the stock isn’t there yet, it starts at 0.
    except ValueError:
        print("❌ Please enter a valid positive integer.")
# Catches any invalid input (e.g., typing a letter instead of a number) and shows an error message.


# Calculate total investment
total_value = 0 
print("\n🧾 Portfolio Summary:")

for stock, qty in portfolio.items(): # Loops through each stock in the portfolio.
    price = stock_prices[stock] # Looks up the price of the stock from stock_prices.
    value = price * qty # Looks up the price of the stock from stock_prices.
    total_value += value # Adds it to the total value.
    print(f"{stock}: {qty} shares x ${price} = ${value}") # it prints stock name  with quantity and also total amount.

print(f"\n💰 Total Investment Value: ${total_value}") # it prints total investment.

# Option to save results
save = input("Do you want to save this summary to a file? (yes/no): ").lower() # Now it asks the user to save file 
if save == "yes":
    filename = "portfolio_summary.txt" # 	This line defines a string variable named filename.
	#"portfolio_summary.txt" is the name of the file where the summary will be saved.

    with open(filename, "w") as file:
        file.write("Stock Portfolio Summary\n")
       # If the answer is "yes", it creates a text file called portfolio_summary.txt.
       # Opens the file in write mode ("w"), which creates the file or overwrites it.

        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares x ${price} = ${value}\n")
            # Writes each stock entry to the file 

        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print(f"✅ Summary saved to '{filename}'")
    # Writes the total investment to the file.
	# Confirms that the file was saved.
