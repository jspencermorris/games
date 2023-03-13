import numpy as np
import random

class Bidder:
    '''
    Represents a Bidder in an Auction.

    Data Attributes defined here:
        num_users (Scalar): the number of User instances in the Auction
        num_rounds (scalar): the number of bidding rounds in the Auction
        balance (scalar): value that represents the Bidder's current
            balance
        last_user (scalar): stores the user_id of the last User engaged
            in the bid() method
        users_auctions (dict): stores the sum scalar each User has been
            drawn by the Auction
        users_bids (dict): stores the Bidder's bid history list for each
            User
        users_wins (dict): stores the win history list for each User
        users_prices (dict): stores the winning/second-place bid history
            list for each User
        users_clicks (dict): shows the click history list for each User
        users_est_prob (dict): stores the estimated click probability
            scalar for each User

    Methods defined here:
        __init__(self,users,bidders):
            Initialize self with num_users Users and num_rounds rounds
        bid():
            Executes bidding strategy and returns a non-negative bid
                value rounded to 3 decimal places
        notify(auction_winner, price, clicked):
            Communicates result of Auction round to the Bidder, where:
            auction_winner (scalar): value is True if Bidder won the
                Auction, False otherwise
            price (scalar): value of the winning (second-price) bid
            clicked (scalar): if the Bidder won the Auction, value is
                True if the User clicked the ad, False otherwise;  if
                the Bidder didn't win the Auction, value is None
    '''
    def __init__(self, num_users=10, num_rounds=1000):
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.balance = 0
        # initialize variables to store useful user-related data
        self.last_user = 0
        self.users_auctions = {}
        self.users_bids = {}
        self.users_wins = {}
        self.users_prices = {}
        self.users_clicks = {}
        self.users_est_prob = {}
    def __repr__(self):
        return self.__class__.__name__
    def __str__(self):
        return f'This is a Bidder object at {id(self)}:\n\t{self.__dict__}'
    def bid(self, user_id):
        '''
        Executes bidding strategy and returns a non-negative bid
            value rounded to 3 decimal places
            1.
            2.
            3.
        '''
        if self.num_rounds > 0 and self.balance > -1000:
            self.num_rounds -= 1
            self.last_user = user_id
            '''
            if self.users_auctions.get(user_id) == None:
                self.users_auctions[user_id] = 1
                # Set an initial estimated probability of None
                self.users_est_prob[user_id] = [None]
            else:
                self.users_auctions[user_id] += 1
                # win_ratio = np.nansum(np.array(self.users_wins[user_id],dtype=np.float)) / sum(self.users_auctions[user_id])
                if np.nansum(np.array(self.users_clicks[user_id],dtype=np.float)) > 1:
                    self.users_est_prob[user_id].append( np.nansum(np.array( \
                        self.users_clicks[user_id], dtype=np.float)) / np.nansum( \
                        np.array(self.users_wins[user_id],dtype=np.float)) )
                else:
                    # Set an initial estimated probability of None
                    self.users_est_prob[user_id].append(None)
            click_ratio = self.users_est_prob[user_id][len(self.users_est_prob[user_id])-1]
            '''
            # print(click_ratio)
            bid_result = 0.5 #np.random.random(1) * np.random.choice([True, False], p=[click_ratio,1-click_ratio])
            # print(f'\t\tvalue of bid result: {bid_result}')
            '''
            if self.users_bids.get(user_id) == None:
                self.users_bids[user_id] = [bid_result]
            else:
                self.users_bids[user_id].append(bid_result)
            '''
            bid_result = round(bid_result, 3)
            return bid_result
    def notify(self, auction_winner, price, clicked):
        '''
        communicates result of Auction round to the Bidder, where:
            auction_winner (scalar): value is True if Bidder won the
                Auction, False otherwise
            price (scalar): value of the winning (second-price) bid
            clicked (scalar): if the Bidder won the Auction, value is
                True if the User clicked the ad, False otherwise;  if
                the Bidder didn't win the Auction, value is None
        '''
        if self.users_wins.get(self.last_user) == None:
            self.users_wins[self.last_user] = [auction_winner]
            self.users_prices[self.last_user] = [price]
            self.users_clicks[self.last_user] = [clicked]
        else:
            self.users_wins[self.last_user].append(auction_winner)
            self.users_prices[self.last_user].append(price)
            self.users_clicks[self.last_user].append(clicked)
        if auction_winner:
            self.balance -= price
        if clicked:
            self.balance += 1
