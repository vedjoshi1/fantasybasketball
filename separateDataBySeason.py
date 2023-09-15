import pandas as pd

# Read the CSV file into a DataFrame
unfilteredData = pd.read_csv('pastSznData.csv')
print(unfilteredData.head())