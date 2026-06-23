"""
Rule-Based Chatbot
------------------
A simple chatbot that responds to predefined user inputs
using if-else logic and keyword matching.

Compatible with Python 3.7+
"""

import random
from datetime import datetime


# ── Rule Engine ──────────────────────────────────────────────────────────────

RULES = [
    {
        "keywords": [
            "hello", "hi", "hey", "howdy", "greetings", "sup",
            "what's up", "whats up", "good morning", "good afternoon",
            "good evening", "morning", "afternoon", "evening", "yo", "hiya"
        ],
        "responses": [
            "Hey there! Great to see you. Type 'help' to see what I can do.",
            "Hello! I'm RuleBot, your rule-based assistant.",
            "Hi! Ready to chat. What's on your mind?",
            "Hey! Good to hear from you. How can I help?",
            "Greetings! What would you like to talk about?",
        ],
    },
    {
        "keywords": [
            "your name", "who are you", "what are you", "call you",
            "are you a bot", "are you human", "are you real", "what is your name",
            "introduce yourself", "who made you", "created you", "built you"
        ],
        "responses": [
            "I'm RuleBot — a chatbot powered by if-else logic. No neural nets, just rules!",
            "The name's RuleBot! I was built with pure Python if-else statements.",
            "I'm RuleBot, a rule-based chatbot. I match keywords and return responses — simple but effective!",
        ],
    },
    {
        "keywords": [
            "how are you", "how's it going", "how do you do", "you okay",
            "how you doing", "you good", "feeling", "are you okay",
            "how have you been", "what's new", "what's going on"
        ],
        "responses": [
            "I'm just a set of if-else statements, but I'm running great!",
            "All my conditions are evaluating correctly — feeling good!",
            "No bugs today, so I'd say I'm doing pretty well!",
            "Running at 100% efficiency. How about you?",
        ],
    },
    {
        "keywords": [
            "help", "what can you do", "commands", "options", "menu",
            "topics", "list", "features", "capabilities", "guide", "instructions"
        ],
        "responses": [
            (
                "Here's what I understand:\n"
                "  • Greetings        → hello, hi, hey, good morning…\n"
                "  • Time & date      → time, date, today, what day…\n"
                "  • Weather          → weather, temperature, forecast…\n"
                "  • Jokes            → joke, funny, make me laugh…\n"
                "  • Math             → calculate, add, multiply…\n"
                "  • Motivation       → motivate, inspire, quote…\n"
                "  • Fun facts        → fact, tell me something, did you know…\n"
                "  • Compliments      → you're great, good bot…\n"
                "  • General chit-chat\n"
                "  • Exit             → bye, exit, quit, goodbye"
            )
        ],
    },
    {
        "keywords": [
            "weather", "temperature", "raining", "sunny", "cold", "hot",
            "forecast", "outside", "climate", "snow", "windy", "storm",
            "cloudy", "humidity", "rain today", "umbrella"
        ],
        "responses": [
            "I'm rule-based, so I can't check live weather — but I hope it's nice where you are!",
            "My if-else logic doesn't include a weather API, but I wish it did!",
            "No live weather access here, but you can check weather.com for updates!",
            "I can't peek outside, but I hope you're not getting rained on!",
        ],
    },
    {
        "keywords": [
            "joke", "funny", "laugh", "humor", "make me laugh",
            "tell me something funny", "comedy", "pun", "hilarious", "cheer me up"
        ],
        "responses": [
            "Why do programmers prefer dark mode?\n→ Because light attracts bugs!",
            "Why did the if-else statement go to therapy?\n→ It had too many conditions.",
            "What do you call a robot that always tells the truth?\n→ An honest-bot!",
            "Why was the Python script sad?\n→ Because it had too many exceptions.",
            "What do you get when you cross a computer and a lifeguard?\n→ A screensaver!",
            "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
            "Why do Java developers wear glasses?\n→ Because they don't C#!",
            "How many programmers does it take to change a light bulb?\n→ None — that's a hardware problem.",
        ],
    },
    {
        "keywords": [
            "thank", "thanks", "appreciate", "cheers", "grateful",
            "ty", "thx", "thank you so much", "many thanks", "much appreciated"
        ],
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "Anytime — that's what rules are for!",
            "No problem at all!",
            "Glad I could assist!",
        ],
    },
    {
        "keywords": [
            "motivat", "inspir", "quote", "encourage", "pick me up",
            "lift me up", "feel better", "positive", "uplifting", "wisdom"
        ],
        "responses": [
            "\"The only way to do great work is to love what you do.\" — Steve Jobs",
            "\"It does not matter how slowly you go as long as you do not stop.\" — Confucius",
            "\"Code is like humor. When you have to explain it, it's bad.\" — Cory House",
            "Every expert was once a beginner. Keep going!",
            "\"First, solve the problem. Then, write the code.\" — John Johnson",
        ],
    },
    {
        "keywords": [
            "fact", "tell me something", "did you know", "interesting",
            "fun fact", "trivia", "random fact", "cool fact", "something cool"
        ],
        "responses": [
            "Did you know? The first computer bug was an actual bug — a moth found in a Harvard computer in 1947!",
            "Fun fact: Python is named after Monty Python, not the snake!",
            "Did you know? There are more possible iterations of a game of chess than atoms in the observable universe.",
            "Fun fact: The average person types about 40 words per minute. A fast typist can do 100+!",
            "Did you know? The first website ever created is still online: info.cern.ch",
            "Fun fact: '00000000' was the actual nuclear launch code for US Minuteman missiles for 8 years during the Cold War.",
        ],
    },
    {
        "keywords": [
            "you're great", "good bot", "well done", "nice", "awesome",
            "you're amazing", "love you", "you're the best", "you rock", "smart bot"
        ],
        "responses": [
            "Aw, thanks! You're making my if-else statements blush.",
            "That means a lot! I'm just doing my keyword matching best.",
            "You're pretty great yourself! 😊",
            "Thanks! I trained hard on these rules.",
        ],
    },
    {
        "keywords": [
            "calculat", "add", "sum", "multiply", "math", "subtract",
            "divide", "plus", "minus", "equation", "what is 2", "what is 1"
        ],
        "responses": [
            "I can do basic math if you type it clearly! Try: 'what is 5 + 3' and I'll do my best.",
            "I'm rule-based, so complex math is tricky — but Python handles it natively if you run `python3 -c 'print(2+2)'`!",
            "Math is tough for a keyword matcher! For calculations, try Python's interactive shell: just type `python3` in your terminal.",
        ],
    },
    {
        "keywords": [
            "sad", "unhappy", "depressed", "down", "upset", "crying",
            "lonely", "stressed", "anxious", "worried", "not okay"
        ],
        "responses": [
            "I'm sorry to hear that. I'm just a bot, but I hope things get better for you soon!",
            "That sounds tough. Remember: it's okay to not be okay. Things usually get better.",
            "Sending virtual good vibes your way. Hope your day improves!",
        ],
    },
]

EXIT_KEYWORDS = [
    "bye", "goodbye", "exit", "quit", "see you", "farewell",
    "later", "cya", "see ya", "take care", "good night", "goodnight", "signing off"
]

EXIT_RESPONSES = [
    "Goodbye! Come back anytime.",
    "See you later! Thanks for chatting with RuleBot.",
    "Bye! Remember: every chatbot misses you in O(1) time.",
    "Take care! It was great chatting with you.",
    "Farewell! My if-else statements will miss you.",
]


def get_time_response():
    now = datetime.now()
    return (
        f"Right now it's {now.strftime('%I:%M %p')} on "
        f"{now.strftime('%A, %B %d, %Y')}."
    )


def get_response(user_input: str) -> tuple:
    """
    Returns (response_text, should_exit).
    Matches user input against rules using keyword search.
    """
    text = user_input.lower().strip()

    # ── Exit check ────────────────────────────────────────────────────────────
    if any(kw in text for kw in EXIT_KEYWORDS):
        return random.choice(EXIT_RESPONSES), True

    # ── Time/date (dynamic response) ─────────────────────────────────────────
    if any(kw in text for kw in ["time", "date", "today", "what day", "clock", "year", "month", "what year"]):
        return get_time_response(), False

    # ── Rule table ────────────────────────────────────────────────────────────
    for rule in RULES:
        if any(kw in text for kw in rule["keywords"]):
            return random.choice(rule["responses"]), False

    # ── Default (no match) ────────────────────────────────────────────────────
    return (
        f"I don't have a rule for that yet. "
        f"My if-else chain didn't match \"{user_input}\". "
        f"Try typing 'help' to see what I understand.",
        False,
    )


# ── Main Loop ─────────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("       RuleBot — Rule-Based Chatbot")
    print("=" * 50)
    print("Hello! I'm RuleBot. Type 'help' to see what")
    print("I can do, or 'bye' to exit.")
    print("-" * 50)

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nRuleBot: Goodbye!")
            break

        if not user_input:
            continue

        response, should_exit = get_response(user_input)
        print(f"RuleBot: {response}\n")

        if should_exit:
            break


if __name__ == "__main__":
    main()
