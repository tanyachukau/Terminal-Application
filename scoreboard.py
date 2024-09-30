import json
import os

class Scoreboard:
    def __init__(self, file_name='high_scores.json'):
        self.file_name = file_name
        self.high_scores = self.load_scores()
        
    def load_scores(self):
        """Load high scores from a file. If no file exists, initialise with 10 default players."""
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, 'r') as file:
                    return json.load(file)
            except (IOError, json.JSONDecodeError):
                print("Error loading high scores. Initialising new scoreboard.")
                return self.initialise_default_scores()
        else:
            return self.initialise_default_scores()
    
    def initialise_default_scores(self):
        """Initialise default high scores with 10 players."""
        default_scores = [{"name": f"Player{i+1}", "score": 0} for i in range(10)]
        self.save_scores(default_scores)
        return default_scores
    
    def save_scores(self, scores):
        """Save high scores to a file."""
        try:
            with open(self.file_name, 'w') as file:
                json.dump(scores, file, indent=4)
        except IOError:
            print("Error saving high scores.")
            
    def update_score(self, player_name, new_score):
        """Update the scoreboard if the player's score is high enough."""
        self.high_scores.append({"name": player_name, "score": new_score})
        
        self.high_scores = sorted(self.high_scores, key=lambda x: x["score"], reverse=True)[:10]
        self.save_scores(self.high_scores)
        
    def display_scores(self):
        """Display the current top high scores."""
        print("\n--- High Scores ---")
        for idx, entry in enumerate(self.high_scores, 1):
            print(f"{idx}. {entry['name']} - {entry['score']}")                      
        