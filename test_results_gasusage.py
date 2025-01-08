import matplotlib.pyplot as plt
import numpy as np

# Data of transaction fees
txn_fees = [0.00000024, 0.00000025, 0.00000023, 0.00000026, 0.00000027, 0.00000026, 0.00000026, 0.00000026]

# Pad the data at the edges to avoid abrupt changes
padded_fees = np.pad(txn_fees, (1, 1), mode='edge')

# Apply a moving average with a small window size to smooth the data
window_size = 3
smoothed_fees = np.convolve(padded_fees, np.ones(window_size) / window_size, mode='valid')

# Generate x-axis values
transactions = range(1, len(txn_fees) + 1)

# Plot the smoothed data
plt.figure(figsize=(6, 4))  # Reduced figure size
plt.plot(transactions, np.array(smoothed_fees) * 1e6, marker='o', linestyle='-', color='green', label='Smoothed Gas Usage')

# Adjust y-axis limits for a "straight-line" appearance
y_min = (np.min(smoothed_fees) - 0.00000001) * 1e6
y_max = (np.max(smoothed_fees) + 0.00000001) * 1e6
plt.ylim(y_min, y_max)

# Graph details
plt.title("Smoothed Gas Usage per Transaction")
plt.xlabel("Transaction Number")
plt.ylabel("Gas Usage (×10⁻⁶ Txn Fee)")  # Adjusted the label to reflect scaling
plt.grid(True, linestyle='--', alpha=0.6)  # Subtle gridlines for a cleaner look
plt.legend()
plt.tight_layout()

plt.savefig('gasUsage.png')

# Show the graph
plt.show()
