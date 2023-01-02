
import pandas as pd

class GameData:

    path = None
    games = None

    def __init__(self):
        self.path = "gamedata.csv"
        try:
            with open("gamedata.csv"):
                self.games = pd.read_csv(self.path, index_col=0)
        except FileNotFoundError:
            self.games = pd.DataFrame(
                columns=[
                    "game_id",
                    "player_1",
                    "player_2",
                    "winner"
                ]
            )

    # Create a new game
    def add_game(self, game_id, player_1, player_2):
        self.games = self.games.append(
            {"game_id": game_id, "player_1": player_1, "player_2": player_2},
            ignore_index=True,
        )
        self.save()

    # Update the winner of a game
    def add_winner(self, game_id, winner):
        game = self.games[self.games["game_id"] == game_id]
        
        if len(game) == 0:
            return False

        self.games.loc[self.games["game_id"] == game_id, "winner"] = winner
        self.save()
        return True
