import numpy as np
import random

class Bidder: # analogous to ...Solver?
    def __init__(self, num_users=10, num_rounds=1000): # I find it strange that the Bidder class defines the number of users and rounds, instead of the Auction
        self.num_users = num_users # the number of User objects in the game
        self.num_rounds = num_rounds # the number of rounts to be played
        self.balance = 1000 # analogous to Game.score
        # initialize the user info
        self.last_user = [] # stores the user_id of the last user engaged in the bid() method
        self.users_auctions = {} # stores the sum scalar each User has been drawn by the Auction
        self.users_bids = {} # stores the Bidder's bid history list for each User
        self.users_wins = {} # stores the win history list for each User
        self.users_prices = {} # stores the winning/second-place bid history list for each User
        self.users_clicks = {} # shows the click history list for each User
        self.users_est_prob = {} # stores the estimated click probability scalar for each User
        # enable round-based analysis in Bidder Class
        '''
        self.rounds_users = []
        self.rounds_bids = []
        self.rounds_wins = []
        self.rounds_prices = []
        self.rounds_clicks = []
        '''
    def __repr__(self):
        return self.__class__.__name__
    def __str__(self):
        return f'This is a Bidder object at {id(self)}:\n\t{self.__dict__}' #  {self.num_users} users & {self.num_rounds} rounds'
    def bid(self, user_id): # returns a non-negative amount of money (round to 3 decimal places)
        if self.num_rounds > 0 and self.balance > 0:
            self.num_rounds -= 1
            self.last_user = user_id
            if self.users_auctions.get(user_id) == None:
                self.users_auctions[user_id] = 1
                self.users_est_prob[user_id] = [0.5] # set an initial estimated probability to 0.5 (which is arbitrary)   <----  this should be made obsolete!
            else:
                self.users_auctions[user_id] += 1
                # win_ratio = np.nansum(np.array(self.users_wins[user_id],dtype=np.float)) / sum(self.users_auctions[user_id])
                if np.nansum(np.array(self.users_clicks[user_id],dtype=np.float)) > 1:
                    self.users_est_prob[user_id].append(np.nansum(np.array(self.users_clicks[user_id],dtype=np.float)) / np.nansum(np.array(self.users_wins[user_id],dtype=np.float)))
                else:
                    self.users_est_prob[user_id].append(None) # set an initial estimated probability to 0.5 (which is arbitrary)   <----  this should be made obsolete!
            ##### here is where the bid strategy goes
            ##### np.nansum(np.array(mydict['user0'],dtype=np.float))   --->   win_ratio = np.nansum(np.array(self.users_wins[user_id],dtype=np.float)) / sum(self.users_auctions[user_id])
            #####
            ##### the decision for the bid amount should be based on:
            #####       0) # of auctions this User has been in, so far (i.e. the opportunity i've had to collect stats)
            #####       1) the win_ratio (i.e. the opportunity i've had to collect ROBUST stats)
            #####     **2) the click_ratio  (i.e. the actual estimated probability, based on my ROBUST stats)
            #####       3) the average winning-price and the most recent winning-price  (i.e. correlation factor based on the hidden stats that others may have but are hidden to me)
            #####       4) the number of remaining rounds
            #####
            epsilon = 0.05
            click_ratio = self.users_est_prob[user_id][len(self.users_est_prob[user_id])-1]
            #print(f'\t\t\tclick_ratio is: {click_ratio}')
            if self.users_clicks.get(self.last_user) == None or sum(filter(None, self.users_clicks[self.last_user])) < 5:
                bid_result = 1
            else:
                if random.random() > epsilon:
                    if click_ratio > 0.5:
                        bid_result = click_ratio
                    else:
                        bid_result = 0
                else:
                    bid_result = 1

            
            
            #print(f'\t\tvalue of bid result: {bid_result}')
            if self.users_bids.get(user_id) == None:
                self.users_bids[user_id] = [bid_result]
            else:
                self.users_bids[user_id].append(bid_result)
            return bid_result
    def notify(self, auction_winner, price, clicked): # used to send info from the round back to the Bidder instance
        ##### consider using 'price' to keep track of all Bidders' behaviors (eventually)?   
        ##### should all of my users dictionaries should be converted to a single 'auction_history' dictionary that stores the data as nested lists?  by round? 
        if self.users_wins.get(self.last_user) == None:
            self.users_wins[self.last_user] = [auction_winner]
            self.users_prices[self.last_user] = [price]
            self.users_clicks[self.last_user] = [clicked]
        else:
            self.users_wins[self.last_user].append(auction_winner)
            self.users_prices[self.last_user].append(price)
            self.users_clicks[self.last_user].append(clicked)
        if clicked:
            self.balance += 1
