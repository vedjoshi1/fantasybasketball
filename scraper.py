
import pandas
from nba_api.stats.endpoints import playerfantasyprofile, playercareerstats, commonplayerinfo
from nba_api.stats.static import players
from constants import player_attribute_vars, historical_training_vars
# Anthony Davis


def get_player_past_stat(id):

    jokicStats = playercareerstats.PlayerCareerStats(id, per_mode36='PerGame')
    jokicDF = jokicStats.get_data_frames()
    jokicSZNs = jokicDF[0]

    inf = {}

    for var in historical_training_vars:
        inf[var] = jokicSZNs[var]

#    print(inf)
    return inf



def get_player_attributes(id):
    mfinfo0 = commonplayerinfo.CommonPlayerInfo(player_id=id)
    mfinfo = mfinfo0.get_data_frames()
    inf = {}

    for var in player_attribute_vars:

        inf[var] = mfinfo[0][var]

    print(inf)
    return inf

def get_player_curr_season_stats_from_name(name):
    llamo = players.find_players_by_full_name(name)
    identification = llamo[0]['id']
    career = playerfantasyprofile.PlayerFantasyProfile(player_id=identification, per_mode36='PerGame')
    overall = career.get_data_frames()[0]

    return overall




