import pandas as pd
import ast
import math
from trainingFunctions import trainPoints
# Read the CSV file into a DataFrame




#Create the X and Y Arrays for our points model. X is everything else from that season, Y is the points
#Do we include name and ID of player? I think we should not.


def get_points(list):
    if not (isinstance(list, str)):



        list = 7;
        return 0 #Find way to make this work better, I don't know if 0 is the right thing to do here
    else:

        listicle = ast.literal_eval(list)
        rVal = listicle[21]
        #print(rVal)
        return rVal








#Issue is that the list is a string, not an array. MUST FIX SOMEHOW
    #fixed




unfilteredData = pd.read_csv('pastSznData.csv')

    #playerIDList = pd.read_csv('playerIDLIST.csv')

    #Here we set the index aside, sort in ascending order, reset index and then remove the rightmost(former index)
index_col = unfilteredData.iloc[:, 0]
unfilteredData = unfilteredData.sort_index(axis=1)
unfilteredData.index = index_col
unfilteredData = unfilteredData.iloc[:, :-1]

    #This will create all of the points databases
pointsDB = unfilteredData.map(get_points)


unfilteredData.fillna(0, inplace=True)
print(unfilteredData) #This is a debugging step to have a breakpoint


#Temporarily calling the training functions from this file, will actually create a file and make it more organized l8r



#have to handle the NaN. Thinking about where there is NaN, in the map function, creating an array w/ the season and all zeroes.
trainPoints(pointsDB, unfilteredData);