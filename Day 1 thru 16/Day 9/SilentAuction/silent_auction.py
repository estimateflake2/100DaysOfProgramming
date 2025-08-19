logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bidder = {}
is_bidding = True
while is_bidding:
    print ("Welcome to the secret auction program!")
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidder[name] = bid
    other_bidders = input ("Are there any other bidders? Type 'yes' or 'no'. ")
    if other_bidders == 'yes':
        print ("\n"*100)
    else:
        is_bidding = False
winner = {"name": "", "bid": 0}

for bid_winner in bidder:
    if winner["bid"] <  int(bidder[bid_winner]):
        winner["name"] = bid_winner
        winner["bid"] = int(bidder[bid_winner])
print (f"The winner is {winner['name']} at bid: ${winner['bid']}")