import numpy as np
from bidder_morris import Bidder as Bidder2a

class User: # analogous to Bandit
    def __init__(self):
        self.__probability = np.random.uniform() # each User has a secret probability of clicking an ad
        self.prob = self.__probability   ##### <------------------------- REMOVE -- CURRENTLY USED IN plot_history()
    def __repr__(self):
        return self.__class__.__name__
    def __str__(self):
        return 'This is a User object w/ secret probability: ' + str(self.__probability)
    def show_ad(self): # represents showing the User object an ad and returning a result for its clicking behavior
        result = np.random.choice([True, False],p=[self.__probability, 1-self.__probability])
        return result

class Auction: # analogous to ...Game (primarily), but also Solver?
    def __init__(self, users, bidders):
        self.users = users # users is a list of all User objects
        self.bidders = bidders # bidders is a list of all Bidder objects
        self.balances = {i:0 for i in range(len(self.bidders))} #{i:1000 for i in range(len(self.bidders))}
        # enable round-based analysis in Auction Class
        self.history = {}
        self.scores = {}
    def __repr__(self):
        return self.__class__.__name__
    def __str__(self):
        return f'This is an Auction object!'
    def execute_round(self): # execute all steps within a single round of the game
        # step 0 - select random user w/ uniform probability
        user_id = np.random.randint(0, len(self.users)) # a user is selected at random
        #print(f'Randomly-chosen User ID is: {user_id}  ---->  ',self.users[user_id])
        ##### consider changing this logic to: 1) consider bidder_id as the unique filename from each Bidder class; 2) make bids a dict, based on bidder_id
        ##### note .pdf says 'It is highly suggested that you make a couple of different Bidder files and run your own 'mock' Auction to test different bidding strategies
        bids = [] # initialize an empty list that will be used to store each bidder's bid
        # steps 1,2,3 - for each bidder, run the bid() method and return a bid-amount
        for bidder_id in range(len(self.bidders)): # each bidder is allowed to return a bid
            if self.balances[bidder_id] < -1000:
                continue
            #print(f'\tbidder_id is:  {bidder_id}')
            ##### left off here in video 7.11.1 @ 8:40  <--yes, he's talking about Users, but should be same principle for Bidders... 
            bids.append(self.bidders[bidder_id].bid(user_id))
        #print(f'Here are all bids from the auction round: {bids}')
        # step 4 - find the winner of the auction based on the bidder w/ the highest bid
        bid_first_price = max(bids)
        winner_candidates = [i for i,j in enumerate(bids) if j == bid_first_price] # create a list of bidders who had the highest bid
        bid_winner = np.random.choice(winner_candidates) # choose a winner randomly if there is a tie
        # step 5 - select the winning price by selecing the second-highest bid
        if len(winner_candidates) > 1:
            bid_second_price = bid_first_price # assign the second-price bid as the first-price bid, if multiple bidders had the same highest bid
        else:
            bids.remove(bid_first_price)
            bid_second_price = max(bids)
        #print(f'Here is the conclusion of the auction round:  Winning Bidder:  {bid_winner}  Second-Price:  {bid_second_price}')
        # steps 6,7 - run show_ad() function of the selected user and return the result for its clicking behavior
        result = self.users[user_id].show_ad()
        #print(f'Did the user click the ad...?  -->  {result}')
        # for each bidder...
        for bidder_id in range(len(self.bidders)):
            # step 8 - if user clicked
            if bidder_id == bid_winner:
                self.bidders[bidder_id].notify(auction_winner=True, price=bid_second_price, clicked=result)
                # step 9 - increase balance dictionary of bidder by 1
                if result:
                    self.balances[bidder_id] += 1 # if user clicked, increase balance dictionary of bidder by 1
                # step 10 - decrease balance dictionary of bidder by the winning price
                self.balances[bidder_id] -= bid_second_price # deplemte the winner's balance by the second_price bid  
            # step 11 - notify losers that they didn't win the winning price
            else:
                self.bidders[bidder_id].notify(auction_winner=False, price=bid_second_price, clicked=None)
        ##### update round-based info for analysis
    def plot_history(self): # optional
        pass

print('='*120); print('='*120)
num_rounds = 1000
num_users = 5
users = [User() for i in range(num_users)]
b0, b1, b2 = Bidder2a(1,num_rounds), Bidder2a(1,num_rounds), Bidder2a(1,num_rounds)
auction = Auction(users, [b0, b1, b2])
for i in range(num_rounds):
    print('^'*40,f'round # {i}','^'*40)
    auction.execute_round()
print('*'*80)
print(b0)
print(b1)
print(b2)
print('*'*80)
auction.plot_history()

print(auction.balances)