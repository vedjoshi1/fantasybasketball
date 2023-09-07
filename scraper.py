
import pandas
from nba_api.stats.endpoints import playerfantasyprofile, playercareerstats
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
# Anthony Davis
career = playerfantasyprofile.PlayerFantasyProfile(player_id='203076', per_mode36='PerGame')
overall = career.get_data_frames()[0]
#print(overall)





variable_data = overall['REB']
#print(variable_data)
# json

#print("Dict")
# dictionary


#print("done")

def get_player_past_stat(id, stat):

    jokicStats = playercareerstats.PlayerCareerStats(id, per_mode36='PerGame')
    jokicDF = jokicStats.get_data_frames()
    jokicSZNs = jokicDF[0]
    jokicData = jokicSZNs[stat]

    return jokicData







def get_player_curr_season_stats_from_name(name):
    llamo = players.find_players_by_full_name(name)
    identification = llamo[0]['id']
    career = playerfantasyprofile.PlayerFantasyProfile(player_id=identification, per_mode36='PerGame')
    overall = career.get_data_frames()[0]

    return overall




