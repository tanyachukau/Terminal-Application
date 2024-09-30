import json
import sys
from datetime import datetime
from tabulate import tabulate
from scoreboard import Scoreboard
from questions import questions_by_category  

# Define classes
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.quiz_history = []
    
    def add_score(self, score, quiz_name):
        self.score += score
        self.quiz_history.append({"quiz": quiz_name, "score": score, "date": str(datetime.now())})
    
    def display_history(self):
        if not self.quiz_history:
            print(f"{self.name} has no quiz history yet.")
        else:
            print(f"Player {self.name}'s Quiz History:")
            print(tabulate(self.quiz_history, headers="keys"))

class Question: 
    def __init__(self, question, correct_answer, choices=None):
        self.question = question
        self.correct_answer = correct_answer
        self.choices = choices  

    def display_question(self):
        if self.choices:

            choices_str = "\n".join([f"{i + 1}. {choice}" for i, choice in enumerate(self.choices)])
            return f"{self.question}\n{choices_str}"
        return self.question

    def check_answer(self, user_answer):
        if self.choices:
            try:
                index = int(user_answer) - 1
                return self.choices[index].lower() == self.correct_answer.lower()
            except (IndexError, ValueError):
                return False
        return user_answer.lower() == self.correct_answer.lower()

class Quiz:
    def __init__(self, player, questions):
        self.questions = questions
        self.player = player

class TimedQuiz(Quiz):
    def __init__(self, player, questions, time_limit):
        super().__init__(player, questions)
        self.time_limit = time_limit
    
    def start(self):
        import time
        start_time = time.time()
        for question_data in self.questions:
            question = question_data['question']
            correct_answer = question_data['answer']
            options = question_data.get('options')
            
            elapsed_time = time.time() - start_time
            if elapsed_time > self.time_limit:
                print(f"Time's up! Your final score is {self.player.score}/{len(self.questions)}")
                break
            
            # Display question and options
            if options:
                print(f"{question}\nOptions:")
                for idx, option in enumerate(options, 1):
                    print(f"{idx}. {option}")
                try:
                    answer_idx = int(input("Choose the correct option (1-4): ")) - 1
                    answer = options[answer_idx]
                except (ValueError, IndexError):
                    print("Please choose a valid option.")
                    continue
            else:
                answer = input(f"{question}: ")

            if answer.lower() == correct_answer.lower():
                print("Correct!")
                self.player.add_score(1, "Timed Space Quiz")
            else:
                print(f"Wrong! The correct answer is {correct_answer}")
            
        print(f"Your final score is: {self.player.score}/{len(self.questions)}")


# Functions
def save_results_to_file(player):
    try:
        with open("quiz_results.json", "w") as file:
            json.dump(player.quiz_history, file, indent=4)
        print("Quiz results saved.")
    except IOError:
        print("An error occurred while saving results.")

def load_player_data():
    try:
        with open("quiz_results.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("No saved data found.")
        return []

# Main menu
def display_main_menu():
    print("Please select a category:")
    print("1. Planets")
    print("2. Stars")
    print("3. Space Missions")
    print("4. Black Holes")
    print("5. Galaxies")

    while True:
        try:
            choice = int(input("Enter the number of the category: "))
            if 1 <= choice <= 5:
                categories = {
                    1: "Planets",
                    2: "Stars",
                    3: "Space Missions",
                    4: "Black Holes",
                    5: "Galaxies"
                }
                return categories[choice]
            else:
                print("Please enter a valid category number (1-5).")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Main execution
if __name__ == "__main__":
    # Get the player's name
    if len(sys.argv) < 2:
        print("Usage: python main.py [player_name]")
        sys.exit(1)
    
    player_name = sys.argv[1]
    player = Player(player_name)

    # Display the main menu and the selected category
    selected_category = display_main_menu()

    # Load questions for the selected category
    category_questions = questions_by_category[selected_category]

    if not category_questions:
        print("No questions available for this category.")
        sys.exit(1)

    # TimedQuiz
    quiz = TimedQuiz(player, category_questions, time_limit=45)

    # Start the quiz and display results
    quiz.start()
    player.display_history()

    # Update and display scoreboard
    scoreboard = Scoreboard()
    scoreboard.update_score(player.name, player.score)
    scoreboard.display_scores()

    # Save results to a file
    save_results_to_file(player)


    







        