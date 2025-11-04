# main.py
import pandas as pd
import os

# Load the dataset
data = pd.read_csv('heart.csv')

# Ensure the "data" directory exists
os.makedirs("data", exist_ok=True)

# Save a copy of the data to the "data" folder
data.to_csv("data/heart.csv", index=False)

print("Data saved to data/heart.csv")
