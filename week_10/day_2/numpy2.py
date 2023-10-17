# Import the NumPy library and alias it as 'np'
import numpy as np

# Define the sales data as a 2D NumPy array
# Each row represents a product, and each column represents a quarter's sales
sales_data = np.array([[500, 600, 750, 900],
                      [300, 350, 400, 450],
                      [200, 250, 300, 350]])

# Define the price per unit as a 1D NumPy array
price_per_unit = np.array([10, 15, 20, 25])

# Calculate the quarterly revenue by performing a dot product between the sales data and price per unit
quaterly_revenue = np.dot(sales_data, price_per_unit)

# Print the resulting quarterly revenue
print(quaterly_revenue)
