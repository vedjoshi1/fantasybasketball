
import pandas
from nba_api.stats.endpoints import playerfantasyprofile
# Anthony Davis
career = playerfantasyprofile.PlayerFantasyProfile(player_id='203076', per_mode36='PerGame')
overall = career.get_data_frames()[0]
print(overall)

variable_data = overall['REB']
print(variable_data)
# json

print("Dict")
# dictionary


print("done")