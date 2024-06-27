import streamlit as st
import matplotlib.pyplot as plt

# Title of your app
st.title('Portfolio Return and Allocation')

# User inputs for returns and weights
stock_return = st.slider('Stock Return (%)', min_value=0.0, max_value=20.0, value=10.0)
stock_weight = st.slider('Stock Weight (%)', min_value=0.0, max_value=100.0, value=60.0)

bond_return = st.slider('Bond Return (%)', min_value=0.0, max_value=20.0, value=5.0)
bond_weight = st.slider('Bond Weight (%)', min_value=0.0, max_value=100.0, value=30.0)

cash_return = st.slider('Cash Return (%)', min_value=0.0, max_value=20.0, value=2.0)
cash_weight = st.slider('Cash Weight (%)', min_value=0.0, max_value=100.0, value=10.0)

# Adjust weights to percentages
total_weight = stock_weight + bond_weight + cash_weight
stock_weight /= total_weight
bond_weight /= total_weight
cash_weight /= total_weight

# Calculate the weighted return of the portfolio
portfolio_return = (stock_return * stock_weight + bond_return * bond_weight + cash_return * cash_weight) / 100

# Display the portfolio return
st.write(f"Total Portfolio Return: {portfolio_return:.2%}")

# Pie chart of allocations
labels = 'Stocks', 'Bonds', 'Cash'
sizes = [stock_weight, bond_weight, cash_weight]
colors = ['gold', 'lightblue', 'lightgreen']
explode = (0.1, 0, 0)  # explode 1st slice

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors)
ax1.axis('equal')

st.pyplot(fig1)
