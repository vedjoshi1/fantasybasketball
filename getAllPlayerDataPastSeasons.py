
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from scraper import get_player_attributes, get_player_past_stat
import pandas as pd

allPlayers = players.get_active_players()

def Merge(dict1, dict2):
    res = dict1 | dict2
    return res

playstatdict = {}

for i in range(len(allPlayers)):
    pid = allPlayers[i]['id']
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=pid)
    player_info = player_info.get_data_frames()
    print(player_info[0]['DISPLAY_LAST_COMMA_FIRST'])
    d1 = get_player_attributes(pid)
    d2 = get_player_past_stat(pid)
    finalplayerDict = Merge(d1,d2)
    playstatdict[pid] = finalplayerDict

frame = pd.DataFrame(playstatdict).T.reset_index()

#frame.to_csv('pastSznData.csv', index=True)

