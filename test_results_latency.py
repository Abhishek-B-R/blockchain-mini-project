import json
import matplotlib.pyplot as plt
from datetime import datetime

# Reading the JSON data from the file
data_points = []
with open("test_results.json", "r") as f:
    for line in f:
        data_points.append(json.loads(line.strip()))

# Filter for 'http_req_duration' metrics that are Points (contain value)
filtered_data = [
    item for item in data_points 
    if item.get("metric") == "http_req_duration" and item.get("type") == "Point"
]

# Extract timestamps and durations
timestamps = [
    datetime.fromisoformat(item['data']['time'][:-6])  # Convert to datetime object
    for item in filtered_data
]
durations = [
    item['data']['value']  # Extract duration values
    for item in filtered_data
]

# Define the filtering time range
start_time = datetime.fromisoformat("2025-01-07T23:41:07")
end_time = datetime.fromisoformat("2025-01-07T23:42:15")

# Filter data points within the time range
filtered_timestamps = [
    timestamps[i] for i in range(len(timestamps)) 
    if start_time <= timestamps[i] <= end_time
]
filtered_durations = [
    durations[i] for i in range(len(timestamps)) 
    if start_time <= timestamps[i] <= end_time
]

# Check if filtered data is non-empty
if filtered_timestamps and filtered_durations:
    # Plot the filtered data
    plt.figure(figsize=(10, 5))
    plt.plot(filtered_timestamps, filtered_durations, marker='o', color='tab:blue')
    plt.title('HTTP Request Duration Over Time (23:41:07 to 23:42:15)')
    plt.xlabel('Time')
    plt.ylabel('Duration (ms)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('http_request_duration_filtered.png')
    plt.show()
else:
    print("No data points found within the specified time range.")
