# for random question generation
import random
# for syllable counting
import nltk

# will keep track of scores
class Player:
    # initialized player name and empty score
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    # increases score based on question points
    def add_to_score(self, points):
        self.score += points
 
# will initiate rounds, keep track of time and rounds, etc.       
class Game:
    
    def __init__(self, num_syllables, num_players):
        self.num_syllables = num_syllables
        self.num_players = num_players
        self.round = 1
        # stores player scores in dict
        self.p_scores = {}
        # keeps track of player's turn
        # set to player 1 at index 0
        self.current_player = 0
        self.game_over = False
        
    def valid_response(self, response):
        # validation logic to be added here
        return True

# will allow players to input their own questions or generate one
# from a pre-populated list of questions 
class Questions:
    # generate q from pre-populated list
    question = [
        ('question1'), 
        ('question2'),
        ('question3'),
        ('question4'),
        ('question5'),
        ...
    ]
    
    # used to select a random question from q's list
    def random_question (self):
        # generates a random number and returns question at that index
        random_number = random.randint(0,len(questions)-1)
        return question[random_number]
