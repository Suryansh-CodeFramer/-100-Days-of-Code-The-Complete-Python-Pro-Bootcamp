import random


def wrong0():


    print("wrong guss 0")
    print(r"""
      +---+
  |   |
      |
      |
      |
      |
=========""")

def wrong1():
    print("wrong guss 1")
    print(r"""
        +---+
  |   |
  O   |
      |
      |
      |
=========
    """)

def wrong2():
    print("wrong guss 2")
    print(r"""
      +---+
  |   |
  O   |
  |   |
      |
      |
=========""")

def wrong3():
    print("wrong guss 3")
    print(r"""
      +---+
  |   |
  O   |
 /|   |
      |
      |
=========""")

def wrong4():
    print("wrong guss 4")
    print(r"""
      +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""")

def wrong5():
    print("wrong guss 5")
    print(r"""
      +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""")

def wrong6():
    print("wrong guss 6")
    print(r"""
      ___________
  |/        |
  |        (_)
  |        \|/
  |         |
  |        / `\`
  |
 _|___""")



def wrong(w):
    if w == 0:
        wrong0()
    elif w == 1:
        wrong1()
    elif w == 2:
        wrong2()
    elif w == 3:
        wrong3()
    elif w == 4:
        wrong4()
    elif w == 5:
        wrong5()
    elif w == 6:
        wrong6()


def words():

    word = [
        # Fruits
        "apple", "banana", "mango", "orange", "grape",
        "papaya", "guava", "peach", "pear", "plum",
        "kiwi", "melon", "lemon", "lime", "cherry",
        "apricot", "fig", "coconut", "lychee", "date",

        # Colors
        "red", "blue", "green", "yellow", "orange",
        "purple", "violet", "indigo", "pink", "brown",
        "black", "white", "gray", "cyan", "magenta",
        "maroon", "beige", "gold", "silver", "olive",

        # Animals
        "tiger", "lion", "zebra", "rabbit", "monkey",
        "giraffe", "elephant", "penguin", "dolphin",
        "cheetah", "leopard", "buffalo", "camel",
        "koala", "panda", "otter", "beaver", "donkey",

        # Countries
        "india", "japan", "canada", "brazil", "france",
        "germany", "mexico", "italy", "spain", "china",
        "egypt", "nepal", "sweden", "norway", "finland",
        "belgium", "turkey", "vietnam", "thailand",

        # Programming
        "python", "java", "kotlin", "swift", "django",
        "flask", "git", "github", "docker", "linux",
        "variable", "boolean", "integer", "string",
        "function", "loop", "array", "object",

        # Sports
        "cricket", "football", "hockey", "tennis",
        "badminton", "boxing", "golf", "cycling",
        "swimming", "karate", "rugby", "volleyball"
    ]
    return word
def logic():


    w=0
    ww=words()
    randomword=random.choice(ww)
    lsrw=list(randomword)
    length = len(randomword)
    print("_ "*length)
    gussword=['_']*length

    print("lets start the game")
    for i in range(0,length):
        guss=input("enter the letter")

        if guss in lsrw:
            for j in range(length):
                if lsrw[j] == guss:
                    gussword[j] = guss

            print(" ".join(gussword))

        else:
            w=w+1
            wrong(w)


    print("the guss is",gussword)

logic()







