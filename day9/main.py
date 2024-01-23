import os


def launch_bid():
    perticipants = []
    keep_going = 'yes'

    while keep_going == 'yes':
        name = str(input("What is your name?: "))
        bid = int(input("What's your bid?: $"))
        perticipants.append({
            'name': name,
            'bid': bid
        })
        keep_going = str(input("Are there any other bidders? Type 'yes' or 'no'.")).lower()
        os.system('cls')
    return perticipants


perticipants = launch_bid()
best_bidder = {'name': '', 'bid': 0}
for p in perticipants:
    best_bidder = p if p['bid'] > best_bidder['bid'] else best_bidder
print(f"{ best_bidder['name'] } win the bid with a bid of ${ best_bidder['bid'] }.")

