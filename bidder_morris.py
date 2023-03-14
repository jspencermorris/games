import numpy as np

class Bidder:
    '''
    Represents a Bidder in an Auction.
    Strategy:  constant bid value

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
        self.num_rounds -= 1
        self.last_user = user_id
        bid_result = 0
        bid_result = round(bid_result,3)
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