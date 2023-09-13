
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from scraper import get_player_attributes, get_player_past_stat
allPlayers = players.get_active_players()

def Merge(dict1, dict2):
    res = dict1 | dict2
    return res



for i in range(2):
    pid = allPlayers[i]['id']
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=pid)
    player_info = player_info.get_data_frames()
    print(player_info[0]['DISPLAY_LAST_COMMA_FIRST'])
    d1 = get_player_attributes(pid)
    d2 = get_player_past_stat(pid)
    finalplayerDict = Merge(d1,d2)
    print(finalplayerDict)

