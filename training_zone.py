from utils.TrainingZoneGame import TrainingZoneGame

if __name__ == "__main__":
    game = TrainingZoneGame("C:/Users/hagsh/OneDrive/Desktop/Self Studies/ML/ml project/images/bg-sand.jpg",
                            500, 700)
    
    while True:
        finish, score = game.play_round()
        
        if finish:
            break
    
    print("Score:", score)
    game.end_pygame()