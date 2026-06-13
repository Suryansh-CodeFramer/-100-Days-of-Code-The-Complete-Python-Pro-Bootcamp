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


def maxFollowers(c1, c2):
    if c1["followers"] > c2["followers"]:
        return c1
    else:
        return c2

def logic():
    while True:
        choice1 = random.choice(people)
        choice2 = random.choice(people)
        if choice1["name"] != choice2["name"]:
            print(choice1 , choice2)
            print(choice1["name"], choice2["name"])
            print(choice1["followers"], choice2["followers"])

            maxFollDic=maxFollowers(choice1,choice2)

            print(f"WHO GOT MORE FOLLOWERS \n\n a: {choice1["name"]} b:{choice2['name']}")
            aa=input("enter who got more followers A or B")
            if aa.lower()=="a":
                if choice1["followers"] ==maxFollDic["followers"]:
                    print("you won")
                    break
                print("wrong guss")
                continue
            elif aa.lower()=="b":
                if choice2["followers"]== maxFollDic["followers"]:
                    print("you Win")
                    break

                print("wrong gusses")
                continue
            else:
                print("wrong pick")
                continue



            # return choice1, choice2


        elif choice1["name"] == choice2["name"]:
            choice2=random.choice(people)


logic()
