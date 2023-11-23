{{PROBLEM}} Class Design Recipe Copy this into a recipe.md in your project and fill it out.

Describe the Problem
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them
I will be using a dictionary to store the information and to pull both the tracks and bands I have listened to.
Design the Class Interface Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

class MyMusic:
# User-facing properties:
# name: string

def __init__(self, name):
# Parameters:
# name: Empty Dictionary
# Side effects:
# None

def add(self, task):
# Parameters:
# task: add artist and track to dictionary
# Returns:
# Nothing
# Side-effects
# Adds artist and track to dictionary
pass # No code here yet

def listened_to(self):
# Returns:
# A dictionary of bands and songs I have listened to
# Side-effects:
# None
Create Examples as Tests Make a list of examples of how the class will behave in different situations.
EXAMPLE
""" Just testing the empty dictionary """

def test_add_to_dict():

""" Check to see if adding multiple bands and tracks workd """

reminder = Reminder("Kay") reminder.remind_me_to("Walk the dog") reminder.remind() # => "Walk the dog, Kay!"

Implement the Behaviour After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.