from utils.TrainingZoneGame import TrainingZoneGame

if __name__ == "__main__":
    game = TrainingZoneGame(640, 480)
    
    while True:
        finish, score = game.play_round()
        
        if finish:
            break
    
    print("Score:", score)
    game.end_pygame()