import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.core.window import Window




### Define our different screens

class TitleScreen(Screen):
    pass

# Define Opening Screen
class DescriptionScreen(Screen):
    pass

class FiveWordsIntroScreen(Screen):
    pass

# Define screen displaying 5 words
class FiveWordsScreen(Screen):
    pass

# Define screen that checks the 5 words
class CheckWordsScreen(Screen):
    pass
    
# Define screen that displays the score of the 5 words test
class DisplayScoreScreen(Screen):
    wordmemorizationscore = StringProperty("")
    pass

# Define Screen 4
class Serial7sIntroScreen(Screen):
    pass

class Serial7sScreen(Screen):
    pass

class Serial7sScoreScreen(Screen):
    serial7sscore = StringProperty("")
    pass

class StroopTestIntroScreen(Screen):
    pass

class StroopTestScreen(Screen):
    pass

# Create the screen manager
class WindowManager(ScreenManager):
    pass

# Connect .kv file
kv = Builder.load_file('dementiadiagnosis.kv')

class DementiaDiagnosisApp(App):
    ### Initialize variables
    correct_words = 0   # Number of words the user got correct in word memorization
    wordmemorizationscore = ""          # Score the user got in word memorization
    checkedwords = []

    serial7numbers = ["93", "86", "79", "72", "65"] # List of correct Serial 7's Test Numbers
    correctnumbers = 0      # Number of correct numbers the user got correct in Serial 7's test
    checkednumbers = []     # List of already checked numbers for Serial 7's

    # Initialize the app
    def build(self):
        self.words = self.generate_random_words()
        return kv

    # Generate random words for the user to type
    def generate_random_words(self):
        # Read in words.txt as word_list
        with open("Dementia Application/words.txt", "r") as file:
            word_list = file.read().splitlines()
        random.shuffle(word_list)
        return word_list[:5]

    # Set words in random list to ids in .kv file
    def on_start(self):
        screen = self.root.get_screen('fivewords')
        screen.ids.word1.text = self.words[0]
        screen.ids.word2.text = self.words[1]
        screen.ids.word3.text = self.words[2]
        screen.ids.word4.text = self.words[3]
        screen.ids.word5.text = self.words[4]
    
    # This function calculates the score every time the user presses enter
    def calculatewordmemorization(self, input_words):
        # Iterates through each word entered by the user (separated by spaces)
        for word in input_words:
            if word in self.words and word not in self.checkedwords:
                self.correct_words += 1
                self.checkedwords.append(word)
        print(self.correct_words)
        #percentage_correct = (correct_words / len(self.words)) * 100
        self.wordmemorizationscore = str(self.correct_words) + "/" + str(len(self.words))
        self.root.get_screen('displayscore').wordmemorizationscore = self.wordmemorizationscore
        return self.wordmemorizationscore

    def calculateserial7s(self, input_nums):
        for num in input_nums:
            if num in self.serial7numbers and num not in self.checkednumbers:
                self.correctnumbers +=1
                self.checkednumbers.append(num)
        print(self.correctnumbers)
        self.serial7sscore = str(self.correctnumbers) + "/" + str(len(self.serial7numbers))
        self.root.get_screen("displayscore").serial7sscore = self.serial7sscore
        return self.serial7sscore


    


# Start running the app when I press play
if __name__ == '__main__':
    DementiaDiagnosisApp().run()
