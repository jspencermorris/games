import numpy as np

class User:
    '''
    Represents a User in an Auction that might click an ad

    Data Attributes defined here:
        __probability (scalar):  the User's secret probability of
            clicking an ad

    Methods defined here:
        __init__(self):
            Initialize self.
        show_ad():
            Returns True if the user clicked the ad, False otherwise
    '''
    def __init__(self):
        self.__probability = np.random.uniform()
    def __repr__(self):
        return self.__class__.__name__
    def __str__(self):
        return 'This is a User object w/ secret probability: ' + str(self.__probability)
    def show_ad(self):
        '''
        Returns True if the user clicked the ad, False otherwise
        '''
        result = np.random.choice([True, False],p=[self.__probability, 1-self.__probability])
        return result

class Auction:
    '''
    Represents a second-price Auction

    Data Attributes defined here:
        users (list): the User instances in the Auction
        bidders (list): the Bidder instances in the Auction
        balances (dict): stores the balance of each Bidder

    Methods defined here:
        __init__(self,users,bidders):
            Initialize self with lists of Users and Bidders
        execute_round():
            Execute all steps in a single Auction round
        plot_history():
            Generate useful information about the Auction results
    '''
    def __init__(self, users, bidders):
        self.users = users
        self.bidders = bidders
        self.balances = {i:0 for i in range(len(self.bidders))} #!#!# set self.balances comprehension to -999 instead of 0;   Line 95 produces a ValueError:  max() arg is an empty sequence
        self.history = {}
    def __repr__(self):
        return self.__class__.__name__
    def __str__(self):
        return f'This is an Auction object!'
    def execute_round(self):
        '''
        Execute all steps in a single Auction round:
            1. Select a user at random w/ uniform probability
            2. For each bidder, run bid() method and return a bid amount
            3. Determine winner of the round
            4. Determine winning price (the second-highest bid)
            5. Run show_ad() method of the user and return the result
                for its clicking behavior
            6. If user clicked, increase balance dictionary of bidder by
                1 and decrease it by the winning price
            7. Run notify() method for each bidder
        '''
        user_id = np.random.randint(0, len(self.users))
        # print(f'Randomly-chosen User ID is: {user_id}  ---->  ',self.users[user_id])
        # Initialize an empty list that will be used to store each \
            # Bidder's bid
        bids = []
        # Each Bidder is allowed to return a bid
        if any(i > -1000 for i in self.balances.values()):
            for bidder_id in range(len(self.bidders)):
                if self.balances[bidder_id] <-1000:
                    continue
                # print(f'\tbidder_id is:  {bidder_id}')
                bids.append(self.bidders[bidder_id].bid(user_id))
            # print(f'Here are all bids from the auction round: {bids}')
            # Find the value of the highest bid
            bid_first_price = max(bids)
            # Create a list of Bidders who had the highest bid
            winner_candidates = [i for i,j in enumerate(bids) if j \
                == bid_first_price]
            # Choose a winner randomly if there is a tie
            bid_winner = np.random.choice(winner_candidates)
            # Select the winning price by finding the second-highest bid
            if len(bids) == 1:
                bid_second_price = bid_first_price
            elif len(winner_candidates) > 1:
                # Asign the second-price as the first-price if multiple \
                    # first-price bids
                bid_second_price = bid_first_price
            else:
                bids.remove(bid_first_price)
                bid_second_price = max(bids)  #!#!# set self.balances comprehension to -999 instead of 0;   Line 95 produces a ValueError:  max() arg is an empty sequence
            # print(f'Here is the conclusion of the auction round:  Winning Bidder:  {bid_winner}  Second-Price:  {bid_second_price}')
            # Run show_ad() method of the selected User and return the result
            result = self.users[user_id].show_ad()
            # print(f'Did the user click the ad...?  -->  {result}')
            # Each Bidder is notified of the Auction round result
            for bidder_id in range(len(self.bidders)):
                # Notify and update balance for winner
                if bidder_id == bid_winner:
                    self.bidders[bidder_id].notify(auction_winner=True, \
                        price=bid_second_price, clicked=result)
                    if result:
                        self.balances[bidder_id] += 1
                    self.balances[bidder_id] -= bid_second_price
                # Notify for losers
                else:
                    self.bidders[bidder_id].notify(auction_winner=False, \
                        price=bid_second_price, clicked=None)
        else:
            raise Exception('No eligible Bidders!')
    def plot_history(self): # optional
        '''
        ....................................................................................................................
        '''
        pass