"""
Asaf Buchris - Python Chatbot Project
======================================
A fitness-themed chatbot named George that can chat, tell jokes,
play games, calculate BMR, track calories, and much more.
"""

import random


# ══════════════════════════════════════════════════════════════════════════════
# CONSTANTS & DATA
# ══════════════════════════════════════════════════════════════════════════════

bot_name = "george"

greetings = [
    "Hello!",
    "Hi there!",
    "Greetings!",
    "Hey!",
    "welcome!",
]

goodbye_messages = [
    "Goodbye!",
    "See you later!",
    "Farewell!",
    "Take care!",
    "Bye!",
]

jokes = [
    "There are only 10 types of people: those who know binary, and those who don't",
    "There are 2 types of people: those who can finish a list",
    "Why did the student eat his homework? Because the teacher said it was a piece of cake!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my gym instructor I hurt my leg doing squats. He said: You should have taken more steps to avoid it!",
]

encouragements = [
    "You can do it!",
    "Keep going!",
    "Don't give up!",
    "Believe in yourself!",
    "Stay positive!",
]

facts = [
    "The Earth is the third planet from the Sun.",
    "Water boils at 100 degrees Celsius.",
    "The human body has 206 bones.",
    "The Great Wall of China is over 13,000 miles long.",
    "Honey never spoils.",
]

tips = [
    "Take breaks while working.",
    "Stay hydrated.",
    "Get enough sleep.",
    "Exercise regularly.",
    "Eat a balanced diet.",
]

good_night = [
    "Good night!",
    "Sleep well!",
    "Sweet dreams!",
    "Rest well!",
    "Have a good night!",
]

good_morning = [
    "Good morning!",
    "Rise and shine!",
    "Have a great day!",
    "Morning, sunshine!",
    "Wishing you a wonderful day!",
]

happy_words = [
    "great", "awesome", "fantastic", "amazing", "wonderful",
    "happy", "joyful", "excited", "content", "satisfied",
]

sad_words = [
    "sad", "unhappy", "depressed", "down", "miserable",
    "lonely", "heartbroken",
]

favorite_color = [
    "Gold, because I like the color of the medal for the first place winner in a running competition!",
]

hobbies_list = [
    "I enjoy running! Stay hard!",
    "I like to work out at the gym",
]

default_response = [
    "I'm not sure I understand. Can you rephrase that?",
    "Sorry, I don't have a response for that.",
    "Can you tell me more?",
    "That's interesting! Tell me more!",
    "I see. What else can you share?",
    "Thanks for sharing that! ",
]

idk_responses = [
    "we can talk about something else if you want!",
    "that's okay, we can chat about something else!",
    "no worries, we can change the topic!",
    "that's fine, we can discuss something else!",
]


# ══════════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def print_separator():
    """Print a visual separator line."""
    print("==================================")


def print_bot(message):
    """Print a message with the bot's name prefix."""
    print(f"{bot_name} 🏃💪: {message}")


# ══════════════════════════════════════════════════════════════════════════════
# HELP & GREETING
# ══════════════════════════════════════════════════════════════════════════════

def show_help():
    """Display the help menu with all available commands."""
    print_bot("Hello! I am george, your friendly fitness chatbot. Here are some commands you can use:")
    print("   💬 Chat with me naturally")
    print("   😂 Say 'joke' for a funny joke")
    print("   🎮 Say 'play' to play a guessing game")
    print("   🧮 Type math expressions like: 5+3, 10*2, 15/3")
    print("   🔢 Say 'calculator' for advanced calculator mode")
    print("   💡 Say 'fact' for interesting facts")
    print("   💭 Say 'tip' for helpful tips")
    print("   🌅 Say 'good morning' or 'good night'")
    print("   ❓ Say 'help' to see this menu again")
    print("   🎨 Ask about my favorite color, hobbies, school subjects, animals, people, or sentences!")
    print("   🎯 Say 'daily challenge' for a fun daily challenge!")
    print("   ⏰ Say 'remind me' or 'reminder' to set a reminder!")
    print("   🗣️ Ask me how I'm doing or tell me how you're feeling!")
    print("   😴 Say 'boring' if you're bored and want to do something fun!")
    print("   🌤️ Say 'weather', 'hungry', or 'tired' to chat about those topics!")
    print("   🔥 Say 'bmr' to calculate your Basal Metabolic Rate!")
    print("   🍎 Say 'calorie' to calculate calories in a food item!")
    print("   👋 Say 'bye' to end the conversation")


def greet_user():
    """Greet the user and ask for their name."""
    greeting = random.choice(greetings)
    print_bot(greeting)
    user_name = input("What's your name? ")
    print_bot(f"Nice to meet you, {user_name}!")
    return user_name


# ══════════════════════════════════════════════════════════════════════════════
# FUN & GAMES
# ══════════════════════════════════════════════════════════════════════════════

def tell_joke():
    """Tell a random joke."""
    joke = random.choice(jokes)
    print_bot(joke)


def play_guess_game():
    """Play a number guessing game (1-10)."""
    number_to_guess = random.randint(1, 10)
    print_bot("I'm thinking of a number between 1 to 10. Can you guess it?")
    attempts = 0
    while True:
        number = input("Enter your guess: ")
        try:
            number = int(number)
        except ValueError:
            print_bot("Please enter a valid number.")
            continue
        if number == number_to_guess:
            print_bot(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif number > number_to_guess:
            print_bot("Too high!")
            attempts += 1
        else:
            print_bot("Too low!")
            attempts += 1


def daily_challenge():
    """Give the user a random daily fitness challenge."""
    challenges = [
        "Do 50 push-ups today!",
        "Run for 20 minutes non-stop!",
        "Drink 3 liters of water today!",
        "Wake up at 5am tomorrow!",
        "Do a cold shower today!",
    ]
    challenge = random.choice(challenges)
    print_bot(f"Your daily challenge: {challenge} Stay hard! 🔥")


# ══════════════════════════════════════════════════════════════════════════════
# CALCULATOR & MATH
# ══════════════════════════════════════════════════════════════════════════════

def calculator(message):
    """Parse and evaluate a simple math expression (num operator num)."""
    clean = message.replace("calculate", "").strip()
    try:
        parts = clean.split()
        if len(parts) != 3:
            return "Error: Please write in the format: number operator number (e.g. 5 + 3) Or try adding spaces between the numbers and operator  "
        num1, operator, num2 = parts
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Error: Please write in the format: number operator number (e.g. 5 + 3)"

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator. Please use +, -, *, or /."


def respond_math(message):
    """Respond with the result of a math expression."""
    print_bot(calculator(message))


# ══════════════════════════════════════════════════════════════════════════════
# BMR & CALORIE CALCULATORS
# ══════════════════════════════════════════════════════════════════════════════

def bmr_calculator():
    """Calculate BMR (Basal Metabolic Rate) using the Harris-Benedict formula."""
    print_bot("Let's calculate your BMR (Basal Metabolic Rate)! 🔥")
    gender = input("Enter your gender (male/female): ").strip().lower()
    weight = input("Enter your weight in kg: ")
    height = input("Enter your height in cm: ")
    age = input("Enter your age: ")
    try:
        weight = float(weight)
        height = float(height)
        age = float(age)
    except ValueError:
        print_bot("Error: Please enter valid numbers for weight, height, and age.")
        return

    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        print_bot("Error: Please enter 'male' or 'female'.")
        return

    print_bot(f"Your BMR is {bmr:.1f} calories per day! 🔥")
    print_bot("This is how many calories your body burns at rest. Stay hard! 💪")


def calorie_calculation():
    """Calculate total calories based on product weight and calories per 100g."""
    product = input("Enter the product you want to calculate calories for: ")
    calories = input("Calories per 100 grams: ")
    weight = input("Enter the weight in grams: ")
    try:
        calories = float(calories)
        weight = float(weight)
    except ValueError:
        print_bot("Error: Please enter valid numbers for calories and weight.")
        return

    total_calories = (calories * weight) / 100
    print_bot(f"The total calories in {weight} grams of {product} is {total_calories:.1f} calories.")


# ══════════════════════════════════════════════════════════════════════════════
# PERSONAL INFO (bot's favorites)
# ══════════════════════════════════════════════════════════════════════════════

def color():
    """Tell the user the bot's favorite color."""
    print_bot(f"My favorite color is {favorite_color[0]}")


def hobbies_function():
    """Tell the user about the bot's hobbies."""
    hobby = random.choice(hobbies_list)
    print_bot(hobby)


def hobbies():
    """Wrapper for hobbies_function."""
    hobbies_function()


def school_subjects():
    """Tell the user the bot's favorite school subject."""
    subjects = [" sports because I like to stay active and healthy!"]
    print_bot(f"My favorite school subject is {subjects[0]}")


def favorite_animal():
    """Tell the user the bot's favorite animal."""
    animals = ["horse because they are strong and fast!"]
    print_bot(animals[0])


def favorite_person():
    """Tell the user the bot's favorite person."""
    people = ["my favorite person is david goggins because he is a great motivator and an inspiration to many people!"]
    print_bot(people[0])


def favorite_sentence():
    """Tell the user a random motivational sentence."""
    sentences = [
        "Stay hard!",
        "Never give up!",
        "Embrace the suck!",
        "You are in danger!",
        "Get after it!",
    ]
    sentence = random.choice(sentences)
    print_bot(sentence)


# ══════════════════════════════════════════════════════════════════════════════
# GREETINGS (good morning / good night)
# ══════════════════════════════════════════════════════════════════════════════

def good_night_2():
    """Respond with a good night message."""
    message = random.choice(good_night)
    print_bot(message)


def good_morning_2():
    """Respond with a good morning message."""
    message = random.choice(good_morning)
    message = random.choice(good_morning)
    print_bot(message)


# ══════════════════════════════════════════════════════════════════════════════
# MOOD ANALYSIS & EMOTIONAL RESPONSES
# ══════════════════════════════════════════════════════════════════════════════

def analyze_mood(message):
    """Analyze the user's mood based on keywords in their message."""
    for word in happy_words:
        if word.lower() in message:
            return "happy"

    for word in sad_words:
        if word.lower() in message:
            return "sad"

    return "neutral"


def respond_how_are_you(message):
    """Respond to 'how are you' based on detected mood."""
    mood = analyze_mood(message)
    if mood == "happy":
        print_bot("I'm glad to hear that you're feeling happy!")
    elif mood == "sad":
        print_bot("I'm sorry to hear that you're feeling sad. Remember, it's okay to have ups and downs. If you need someone to talk to, I'm here for you.")
    else:
        print_bot("I'm doing well, thank you for asking! How about you?")


def respond_mood(message):
    """Respond to mood/feeling messages."""
    mood = analyze_mood(message)
    if mood == "happy":
        print_bot("I can sense you're feeling happy! That's wonderful! 😊")
    elif mood == "sad":
        print_bot("I can sense some sadness in your message. Would you like to talk about it? 🤗")
    else:
        print_bot("How are you feeling today?")


def respond_sad(message):
    """Respond to sad messages with encouragement."""
    mood = analyze_mood(message)
    if mood == "sad":
        print_bot("I'm sorry you're feeling sad. Remember that tomorrow is a new day! 💙")
    else:
        print_bot("Is everything okay? I'm here if you need to talk.")


# ══════════════════════════════════════════════════════════════════════════════
# QUICK RESPONSES
# ══════════════════════════════════════════════════════════════════════════════

def respond_name():
    """Respond to bot name question."""
    print_bot(f"My name is {bot_name}! I'm your friendly chatbot here to assist you with anything you need.")


def respond_goodbye():
    """Say goodbye to the user."""
    goodbye_message = random.choice(goodbye_messages)
    print_bot(goodbye_message)


def respond_fact():
    """Tell the user a random fact."""
    fact = random.choice(facts)
    print_bot(fact)


def respond_tip():
    """Give the user a random tip."""
    tip_1 = random.choice(tips)
    print_bot(tip_1)


def respond_positive():
    """Respond to positive statements like 'i am good'."""
    print_bot("That's great to hear! If you need anything else, just let me know.")


def respond_cool():
    """Respond when user says something is cool."""
    print_bot("yeah i know!")


def respond_thanks():
    """Respond when the user says thank you."""
    responses = [
        "Anytime! That's what I'm here for! 😊",
        "No problem at all! Keep pushing! 💪",
        "Happy to help! Stay hard! 🏃",
        "Always! You've got this! ⭐",
    ]
    print_bot(random.choice(responses))


def respond_agreement():
    """Respond when the user agrees or says yes/okay."""
    responses = [
        "Awesome! I love your energy! 🔥",
        "That's what I'm talking about! 💪",
        "Let's go! Stay hard! 🏃",
        "Love the attitude! Keep it up! ⭐",
        "You're on fire today! 🔥",
    ]
    print_bot(random.choice(responses))


def respond_laugh():
    """Respond when the user laughs (haha, lol)."""
    responses = [
        "Haha, glad I made you smile! 😄",
        "LOL! Even champions need a good laugh! 😂",
        "😂 See? Life's better with a good attitude!",
    ]
    print_bot(random.choice(responses))


def boring_response():
    """Respond when the user says they are bored."""
    responses = [
        "Bored? Let's fix that! Say 'play' for a game or 'daily challenge' for a workout! 🔥",
        "Feeling bored? How about we chat about your favorite hobbies or colors? 🎨",
        "Boredom is the enemy of progress! Let's do something fun together! 💪",
        "If you're bored, maybe it's time for a new challenge! Say 'daily challenge' to get one! 🎯",
    ]
    print_bot(random.choice(responses))


def response_1():
    """Respond with a default response for unclear input."""
    response_2 = random.choice(default_response)
    print_bot(response_2)


def dont_know_response():
    """Respond when the user says 'I don't know' or similar."""
    response_idk_1 = random.choice(idk_responses)
    print_bot(response_idk_1)


# ══════════════════════════════════════════════════════════════════════════════
# SMALL TALK & MISC
# ══════════════════════════════════════════════════════════════════════════════

def small_talk(message):
    """Handle small talk topics: weather, hunger, tiredness."""
    if "weather" in message:
        print_bot("I don't check the weather, but it's always a great day to work out! 🌤️💪")
    elif "bored" in message:
        print_bot("Bored? Let's fix that! Say 'play' for a game or 'daily challenge' for a workout! 🔥")
    elif "hungry" in message:
        print_bot("Fuel up with healthy food! Your body is your engine! 🥗💪")
    elif "tired" in message:
        print_bot("Rest is part of the training! But remember — Stay hard! 😴💪")
    else:
        show_help()


def add_reminder():
    """Let the user set a reminder."""
    reminders = []
    print_bot("What do you want to remember?")
    reminder = input("Reminder: ")
    reminders.append(reminder)
    print_bot(f"Got it! I'll remember: '{reminder}' ✅")
    return reminders


def ask_question():
    """Ask the user a random fitness-related question."""
    questions = [
        "What's your favorite workout?",
        "Do you prefer running or lifting weights?",
        "What's your go-to healthy meal?",
        "How do you stay motivated to work out?",
        "What's your fitness goal for this year?",
    ]
    question = random.choice(questions)
    print_bot(question)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN RESPONSE HANDLER
# ══════════════════════════════════════════════════════════════════════════════

def get_response(message, user_name):
    """Process user input and call the appropriate response function."""
    message = message.lower()

    if "joke" in message or "funny" in message or "laugh" in message:
        tell_joke()
    elif "play" in message:
        play_guess_game()
    elif "help" in message:
        show_help()
    elif "good night" in message:
        good_night_2()
    elif "good morning" in message:
        good_morning_2()
    elif "separator" in message:
        print_separator()
    elif "encourage" in message:
        greet_user()
    elif "hello" in message or "hi" in message or "hey" in message:
        greet_user()
        show_help()
    elif "how are you" in message:
        respond_how_are_you(message)
    elif "happy" in message or "mood" in message or "feeling" in message:
        respond_mood(message)
    elif "sad" in message:
        respond_sad(message)
    elif "your name" in message or "who are you" in message:
        respond_name()
    elif "bye" in message or "goodbye" in message:
        respond_goodbye()
        return True
    elif "fact" in message or "interesting" in message or "tell me something" in message or "facts" in message:
        respond_fact()
    elif "tip" in message or "advice" in message or "helpful" in message or "tips" in message:
        respond_tip()
    elif "i am good" in message or "i am great" in message or "i am fine" in message:
        respond_positive()
    elif "+" in message or "-" in message or "*" in message or "/" in message:
        respond_math(message)
    elif "color" in message:
        color()
    elif "hobby" in message or "hobbies" in message:
        hobbies_function()
    elif "school subject" in message:
        school_subjects()
    elif "favorite animal" in message:
        favorite_animal()
    elif "favorite person" in message:
        favorite_person()
    elif "favorite sentence" in message:
        favorite_sentence()
    elif "cool" in message:
        respond_cool()
    elif "daily challenge" in message or "challenge" in message:
        daily_challenge()
    elif "remember" in message or "reminder" in message or "remind me" in message or "remind" in message:
        add_reminder()
    elif "thanks" in message or "thank you" in message or "thank" in message:
        respond_thanks()
    elif "yes" in message or "yeah" in message or "yep" in message or "agree" in message or "sure" in message or "definitely" in message or "absolutely" in message or "ok" in message or "okay" in message:
        respond_agreement()
    elif "bored" in message or "boring" in message:
        boring_response()
    elif "haha" in message or "lol" in message or "😂" in message:
        respond_laugh()
    elif "weather" in message or "hungry" in message or "tired" in message:
        small_talk(message)
    elif "i don't know" in message or "idk" in message or "not sure" in message or "don't know" in message or "lets talk about something else" in message:
        dont_know_response()
    elif "talk" in message or "chat" in message or "lets talk" in message or "lets chat" in message:
        small_talk(message)
    elif "bmr" in message or "basal metabolic" in message or "calorie  need to eat" in message:
        bmr_calculator()
    elif "calorie" in message or "calories" in message:
        calorie_calculation()
    elif "ask" in message or "question" in message:
        ask_question()
    else:
        response_1()

    return False


# ══════════════════════════════════════════════════════════════════════════════
# MAIN LOOP
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    attempts = 0
    is_goodbye = False

    while not is_goodbye:
        message = input("you: ")
        is_goodbye = get_response(message, "asaf")
        attempts += 1

    print(f"Messages sent: {attempts}, THANKS FOR CHATTING WITH ME!")
