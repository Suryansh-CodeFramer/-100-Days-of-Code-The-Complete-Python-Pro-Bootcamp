print(" number of bidders ")
No_of_Bidders = int(input())
bidders = {}
for i in range(No_of_Bidders):
    Bid_or_not=input("would you like to bid? y for yes or n for no")
    if Bid_or_not=="y":
        name=input("what is your name? ")
        bid=int(input("what is your bid? "))
        bidders[name] = bid
        print("\n"*150)
    else:
        continue

highest_bidder_name = ""
highest_bidder_value = 0

for key in bidders:
    if bidders[key] > highest_bidder_value:
        highest_bidder_value = bidders[key]
        highest_bidder_name = key

print(f"The winner is {highest_bidder_name} with a bid of ${highest_bidder_value}")

bid_winner=highest_bidder_name
