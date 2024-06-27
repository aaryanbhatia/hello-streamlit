import matplotlib.pyplot as plt

# Define the assets in the portfolio with their returns and weights
assets = {
    'Stocks': {'return': 0.10, 'weight': 0.60},  # 10% return, 60% of the portfolio
    'Bonds': {'return': 0.05, 'weight': 0.30},   # 5% return, 30% of the portfolio
    'Cash': {'return': 0.02, 'weight': 0.10}     # 2% return, 10% of the portfolio
}

# Calculate the weighted return of the portfolio
portfolio_return = sum(asset['return'] * asset['weight'] for asset in assets.values())

# Labels for the sectors
labels = assets.keys()

# Sizes for each slice
sizes = [asset['weight'] for asset in assets.values()]

# Colors for each sector
colors = ['gold', 'lightblue', 'lightgreen']

# Exploding the 1st slice (stocks)
explode = (0.1, 0, 0)

# Plotting the Pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the total portfolio return and show the pie chart
print(f"Total Portfolio Return: {portfolio_return:.2%}")
plt.show()
