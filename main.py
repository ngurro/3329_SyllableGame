# for random question generation
import random
# for syllable counting
import nltk
from nltk.corpus import words,cmudict


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
        # checks if word is in English
        if response.lower() not in words.words():
            return False
        # checks if it is just a one letter word
        if len(response.split()) == 1;
            return False
        # checks if response has exceeded the amount of syllables
        if self.get_syllables(response) > self.num_syllables
            return False
        return True
        
    def play_round(self):
     pass

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
    def __init__(self):
        self.dictionary = nltk.corpus.cmudict.dict()
        # used to select a random question from q's list
        def random_question (self):
            # generates a random number and returns question at that index
            random_number = random.randint(0,len(self.question)-1)
            return self.question[random_number]
    
         # function used to get syllable amount from answer (Note:idk where to put this yet)
        def get_syllables(self, answer):
        syllables = 0
        for word in answer.split():
            syllables += len(self.dictionary.get(word.lower(), [[0]])[0])
        return syllables
