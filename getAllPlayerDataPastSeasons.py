
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

for i in range((50)):
    pid = allPlayers[i]['id']
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=pid)
    player_info = player_info.get_data_frames()
    print(player_info[0]['DISPLAY_LAST_COMMA_FIRST'])
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

#Make PlayerID the key for the dict, to allow us to find a player
#Make the dictionary value a dictionary of each season's statistics, with Season_ID as the key, and the
#value being a list of the season's stats
#This will allow us to filter by player and Season
#Find a way to extract points LATER, also consider changing scraper to simply return a dictionary of seasons


frame = pd.DataFrame(playstatdict).T.reset_index()
#frame.to_csv('pastSznData.csv', index=False)

