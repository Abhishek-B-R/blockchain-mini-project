import matplotlib.pyplot as plt
import numpy as np

# Simulated data
time = np.arange(0, 60, 1)  # Time in seconds (0 to 60 seconds)
valid_request_counts = [np.sin(0.1 * t) * 10 + 50 + np.random.randint(-5, 5) for t in time]
invalid_request_counts = [np.random.randint(0, 10) for _ in time]

# Create the plot
plt.figure(figsize=(12, 6))

# Scatter plot for valid requests
plt.scatter(time, valid_request_counts, label="Valid Requests", color="green", alpha=0.7)

# Scatter plot for invalid requests
plt.scatter(time, invalid_request_counts, label="Invalid Requests", color="red", alpha=0.7)

# Adding titles and labels
plt.title("HTTP Request Counts Over Time", fontsize=14)
plt.xlabel("Time (seconds)", fontsize=12)
plt.ylabel("Request Counts", fontsize=12)

# Add grid and legend
plt.grid(alpha=0.5)
plt.legend(fontsize=12)
plt.tight_layout()

plt.savefig('valid_http_request_throughput.png')
# Display the plot
plt.show()
