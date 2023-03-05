def count_retweets_by_username(tweet_list):
    """ (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """
    usernames = []
    for tweet in tweet_list:
        if 'RT @' in tweet:
            # isolate only the twitter username and append to the list
            usernames.append(tweet.split('RT @')[1].split(':')[0])
    retweets = {}
    for username in usernames:
        # count the number of times each username is an element in the list
        if username in retweets:
            retweets[username] += 1
        else:
            retweets[username] = 1
    return retweets

def display(deposits, top, bottom, left, right):
    """display a subgrid of the land, with rows starting at top and up to 
    but not including bottom, and columns starting at left and up to but
    not including right."""
    # generate an initial grid of the required size with no X's
    grid = [['-' for j in range(left,right)] for i in range(top,bottom)]
    for deposit in deposits:
        # identify deposits of acceptable coordinates within the input list
        if top<=deposit[0]<bottom and left<=deposit[1]<right:
            # denote coordinate's of identified deposits with an X
            grid[deposit[0]-top][deposit[1]-left] = 'X'
    ans = ''
    # generate a string object based on the grid list
    for row in grid:
        for character in row:
            ans += character
        ans += '\n'
    return ans

def tons_inside(deposits, top, bottom, left, right):
    """Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right."""
    tonnage = 0
    for deposit in deposits:
        # identify deposits of acceptable coordinates within the input list
        if top<=deposit[0]<bottom and left<=deposit[1]<right:
            # add the deposit value of identified deposits to the tonnage
            tonnage += deposit[2]    
    return tonnage

def birthday_count(dates_list):
    """Returns the total number of birthday pairs in the dates_list"""
    bday_counts = {}
    # geenrate a dict that stores the frequencies of each bday
    for date in dates_list:
        if date in bday_counts:
            bday_counts[date] += 1
        else:
            bday_counts[date] = 1
    bday_replicates = 0
    # sum up all replicated bdays
    for count in bday_counts.values():
        if count > 1:
            bday_replicates += count
    return bday_replicates
