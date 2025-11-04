# # main.py ......version 1
# import pandas as pd
# import os

# # Load the dataset
# data = pd.read_csv('heart.csv')

# # Ensure the "data" directory exists
# os.makedirs("data", exist_ok=True)

# # Save a copy of the data to the "data" folder
# data.to_csv("data/heart.csv", index=False)

# print("Data saved to data/heart.csv")


# main.py ......version 2
import pandas as pd
import os

# Load the dataset
data = pd.read_csv('heart.csv')

# Remove the 'thalach' column (if it exists)
if 'thalach' in data.columns:
    data = data.drop(columns=['thalach'])
    print("'thalach' column removed successfully.")
else:
    print("thalach' column not found in dataset.")

# Ensure the "data" directory exists
os.makedirs("data", exist_ok=True)

# Save the modified data
data.to_csv("data/heart.csv", index=False)

print("Updated data (without 'thalach') saved to data/heart.csv")
