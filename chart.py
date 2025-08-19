# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")  # Presentation-ready text sizes

# Generate synthetic data
np.random.seed(42)
num_customers = 100
acquisition_cost = np.random.normal(200, 50, num_customers)
lifetime_value = acquisition_cost * np.random.uniform(1.5, 5.0, num_customers)

# Create DataFrame
data = pd.DataFrame({
    "Acquisition_Cost": acquisition_cost,
    "Lifetime_Value": lifetime_value
})

# Create scatterplot
fig = plt.figure(figsize=(8, 8), dpi=64)  # 8x8 inches × 64 dpi = 512x512 px
ax = sns.scatterplot(
    x="Acquisition_Cost",
    y="Lifetime_Value",
    data=data,
    color="royalblue",
    s=100,
    edgecolor="k"
)

# Add title and labels
ax.set_title("Customer Lifetime Value vs Acquisition Cost")
ax.set_xlabel("Acquisition Cost ($)")
ax.set_ylabel("Customer Lifetime Value ($)")

# Adjust layout to avoid cropping
plt.tight_layout()

# Save figure exactly 512x512 pixels
fig.savefig("chart.png", dpi=64)
plt.close()
