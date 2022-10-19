import sys

from utils.TrainingZoneGameAuto import TrainingZoneGameAuto
from utils.TrainingZoneGameByHand import TrainingZoneGameByHand

games = {
    "htz": TrainingZoneGameByHand(),
    "atz": TrainingZoneGameAuto()
}

if __name__ == "__main__":
    game = games[sys.argv[1]]
    
    while True:
        finish, score = game.play_round()
        
        if finish:
            break
    
    print("Score:", score)
    input("Press any key to quit")
    game.end_pygame()