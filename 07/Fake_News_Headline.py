import random

subjects = [
    "Sharukh khan",
    "Virat kohli",
    "Nirmala Sitaraman",
    "A mubai Cat",
    "A group of Monkey",
    "Auto Rickshaw Driver From Delhi",
]

actions = [
    "launches",
    "cancels",
    "dances in",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai local Train",
    "a plate of samosa",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]



while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    palce_or_thing = random.choice(places_or_things)


    headline = f"BREAKING NEWS: {subject} {action} {palce_or_thing}"
    print ("\n" + headline)

    user_input = input("\n Do you want another headline? (Y/N)").strip().lower()
    if user_input == "n":
        break

    print("\n Thanks for using the Fake News Headline Generator. Have a fun day")