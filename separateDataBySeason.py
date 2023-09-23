import pandas as pd

# Read the CSV file into a DataFrame
unfilteredData = pd.read_csv('pastSznData.csv')

#playerIDList = pd.read_csv('playerIDLIST.csv')

#Here we set the index aside, sort in ascending order, reset index and then remove the rightmost(former index)
index_col = unfilteredData.iloc[:, 0]
unfilteredData = unfilteredData.sort_index(axis=1)
unfilteredData.index = index_col
unfilteredData = unfilteredData.iloc[:, :-1]


#Create the X and Y Arrays for our points model. X is everything else from that season, Y is the points
#Do we include name and ID of player? I think we should not.


def get_points(list):

    return list[21]

listicle = unfilteredData.at[ 1630173,'2020-21']
points = listicle[21]
print(points)

#Issue is that the list is a string, not an array. MUST FIX SOMEHOW

pointsDB = unfilteredData.applymap(get_points)
print(unfilteredData) #This is a debugging step to have a breakpoint

