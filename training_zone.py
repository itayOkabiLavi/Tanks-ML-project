from utils.TrainingZoneGame import TrainingZoneGame

if __name__ == "__main__":
    game = TrainingZoneGame("C:/Users/hagsh/OneDrive/Desktop/Self Studies/ML/ml project/images/bg-sand.jpg")
    
    while True:
        finish, score = game.play_round()
        
        if finish:
            break
    
    print("Score:", score)
    input("Press any key to quit")
    game.end_pygame()