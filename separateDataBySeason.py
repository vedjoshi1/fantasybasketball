import pandas as pd

# Read the CSV file into a DataFrame
unfilteredData = pd.read_csv('pastSznData.csv')

#playerIDList = pd.read_csv('playerIDLIST.csv')

#unfilteredData = unfilteredData.set_index(playerIDList['0'])
print(unfilteredData)

#maybe fix order of columns, make them go year-by-year. This is not a priority. 