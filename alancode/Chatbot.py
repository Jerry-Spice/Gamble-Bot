#############################################
# Chatbot starter code
#############################################

#import random number generator methods
import random

#define Chatbot class
class Chatbot:
  def __init__(self, name, phrases):
    self.name=name
    self.phrases = phrases
  
  def chat(self):
    num = random.randint(0, len(self.phrases)-1)
    return self.name + " says: "+ self.phrases[num]
    
#create a list of phrases for Chatbot Bob
bobPhrases = ["Hello", "How are you?", "Are you okay?"]

#create the "bob" instance of Chatbot
bob = Chatbot("Bob", bobPhrases)

#get the user's name
name = input("What is your name? ")

bot2Phrases = ["How's the weather?","What's your favorite color?","What is your mother's maiden name?"]
bot2 = Chatbot(name, bot2Phrases)

# #print a random response from bob
# print name + ", " + bob.name + " says " + bob.chat()

while True:
  print(bob.chat())
  input()
  print(bot2.chat())
  input()
