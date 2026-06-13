import random

people = [
    {"name": "Cristiano Ronaldo", "followers": 650_000_000},
    {"name": "Lionel Messi", "followers": 505_000_000},
    {"name": "Selena Gomez", "followers": 420_000_000},
    {"name": "Kylie Jenner", "followers": 395_000_000},
    {"name": "Dwayne Johnson", "followers": 395_000_000},
    {"name": "Ariana Grande", "followers": 375_000_000},
    {"name": "Kim Kardashian", "followers": 360_000_000},
    {"name": "Beyoncé", "followers": 315_000_000},
    {"name": "Khloé Kardashian", "followers": 300_000_000},
    {"name": "Justin Bieber", "followers": 295_000_000},
    {"name": "Taylor Swift", "followers": 285_000_000},
    {"name": "Kendall Jenner", "followers": 285_000_000},
    {"name": "Jennifer Lopez", "followers": 250_000_000},
    {"name": "Virat Kohli", "followers": 275_000_000},
    {"name": "Neymar Jr", "followers": 230_000_000},
    {"name": "Nicki Minaj", "followers": 225_000_000},
    {"name": "Miley Cyrus", "followers": 215_000_000},
    {"name": "Katy Perry", "followers": 205_000_000},
    {"name": "Zendaya", "followers": 185_000_000},
    {"name": "Kevin Hart", "followers": 180_000_000},
    {"name": "Shakira", "followers": 170_000_000},
    {"name": "LeBron James", "followers": 160_000_000},
    {"name": "Billie Eilish", "followers": 125_000_000},
    {"name": "Shraddha Kapoor", "followers": 95_000_000},
    {"name": "Narendra Modi", "followers": 92_000_000},
    {"name": "Priyanka Chopra", "followers": 92_000_000},
    {"name": "Alia Bhatt", "followers": 86_000_000},
    {"name": "Deepika Padukone", "followers": 80_000_000},
    {"name": "Elon Musk", "followers": 65_000_000},
    {"name": "MrBeast", "followers": 70_000_000}
]


def random_item_picking(c1, c2):
    while True:
        choice1 = random.choice(people)
        choice2 = random.choice(people)
        if choice1["name"] != choice2["name"]:
            return choice1, choice2

        elif choice1["name"] == choice2["name"]:
            choice2=random.choice(people)
c1,c2=random_item_picking(c1={},c2={})

def logic():
