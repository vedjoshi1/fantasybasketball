import json
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from scraper import get_player_attributes, get_player_past_stat
import pandas as pd
from constants import historical_training_vars

allPlayers = players.get_active_players()

def Merge(dict1, dict2):
    res = dict1 | dict2
    return res

playstatdict = {}
#playerID = []
for i in range((100)):
    pid = allPlayers[i]['id']
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=pid)
    player_info = player_info.get_data_frames()
   # print(player_info[0]['DISPLAY_LAST_COMMA_FIRST']) #Must comment this out later, leave it now as a status indicator
  #  print(pid)
    d1 = get_player_attributes(pid)
    d2 = get_player_past_stat(pid)
    seasonsDict = {}
    for j in range(len(d2['SEASON_ID'])):
       seasonStats = []
       for var in historical_training_vars:
           seasonStats.append(d2[var][j])


       seasonStats.append(d1.values())

       seasonsDict[d2['SEASON_ID'][j]] = seasonStats





    playstatdict[pid] = seasonsDict
  ##  playerID.append(pid)


#Made PlayerID the key for the dict, to allow us to find a player
#Made the dictionary value a dictionary of each season's statistics, with Season_ID as the key, and the
#value being a list of the season's stats
#This allows us to filter by player and Season
#Find a way to extract points LATER, also consider changing scraper to simply return a dictionary of seasons

#find a better way to convert this dict to pandas, or maybe don't even do it yet


    #Have found a solution that allows the database to be saved properly into the .csv file. Will need to perhaps fine tune it later,
    #but is a good solution for now

#frame = pd.DataFrame(playstatdict)
df = pd.DataFrame.from_dict(playstatdict, orient='index')
#ids = pd.DataFrame(playerID)


df.to_csv('pastSznData.csv', index=True)

