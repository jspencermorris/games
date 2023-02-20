from wordscore import score_word
    
def run_scrabble(rack):
    """
    Given an input scrabble rack of up to 7 characters...
    
    returns all 'valid scrabble English' words that can be constructed
    from that rack, along with their scrabble scores, sorted by score
    
    returns the total number of 'valid scrabble English' words
    """
    
    rack = sorted(rack.upper())
    
    # return helpful messages for common user-input errors
    if len(rack)<2:
        return('You entered fewer than 2 characters')
    if len(rack)>7:
        return('You entered more than 7 letters')
    import string
    for char in rack:
        if char not in string.ascii_uppercase+'*'+'?':
            return('You entered an invalid character.  Please use only letters or wildcards (* & ?)')
    if ''.join(rack).count('*') > 1 or ''.join(rack).count('?') >1:
        return('You entered more than one wildcard instance (* or ?)')
    
    # read the sowpod file of valid scrabble words and store them as a list
    with open('sowpods.txt','r') as infile:
        raw_input = infile.readlines()
        sowpods_words = [sowpods_word.strip('\n') for sowpods_word in raw_input]
    
    """
    find valid words by looping through the list of sowpods words,  
    creating temporary lists to store chars in the sowpods word and rack,
    comparing the characters in the sowpod word to the characters in the rack,
    removing matching characters from the temp lists,
    and if the number of remaining characters doesn't exceed the number of available wildcards,
    append the sowpods word to the valid_words list
    and append the wildcard chars to the invalid_chars list
    """
    valid_words = [] # initialize an empty list to store all valid words
    invalid_chars = [] # initialize an empty list to store lists chars from wildcards
    for word in sowpods_words:
        temp_rack = list(rack) # for each iter, create a list of chars in the rack
        temp_word = list(word) # for each iter, create a list of chars in the word
        for letter in word:
            # remove matching characters from the tempoerary lists
            if letter in temp_rack:
                temp_rack.remove(letter)
                temp_word.remove(letter)
        # check if there are fewer remaining characters than available wildcards
        if len(temp_word) - temp_rack.count('?') - temp_rack.count('*') <= 0:
            valid_words.append(word) # append the word
            invalid_chars.append(temp_word) # append the list of characters from wildcards

    # scoring
    score_list = [] # create a list to store the words and their scores
    # calculate the scores of the sowpods word minus the chars from wildcards
    for word,wildcards in zip(valid_words,invalid_chars):
        score_list.append((score_word(word)-score_word(wildcards),word))
    score_list = sorted(score_list, key=lambda option: option[0], reverse=True)
    valid_num = len(score_list)

    return score_list, valid_num