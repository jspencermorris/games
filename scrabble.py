def run_scrabble(rack):
    """run_scrabble takes a scrabble rack as a function argument and prints all
    'valid scrabble English' words that can be constructed from that rack,
    along with their scrabble scores, sorted by score"""
    print('calling run_scrabble...')
    
    rack = sorted(rack.upper())
    
    # step 0: error handling
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
    
    # step 1 - read the sowpod list of valid scrabble words
    with open('sowpods.txt','r') as infile:
        raw_input = infile.readlines()
        sowpods_words = [sowpods_word.strip('\n') for sowpods_word in raw_input]

    ##! step 2 - 'get the rack' as a parameter from the terminal 
    # - eg. run:    python scrabble ZAEfiee
    # currently this is being handled outside this function
    
    # step 3 - find valid words
    valid_words = []
    for word in sowpods_words:
        temp_rack = list(rack)
        temp_word = list(word)
        for letter in word:
            if letter in temp_rack:
                temp_rack.remove(letter)
                temp_word.remove(letter)
        if len(temp_word) - temp_rack.count('?') - temp_rack.count('*') <= 0:
            valid_words.append(word)
            # also need to create a valid_letters list that only includes valid ones for scoring

    # step 4 - scoring
    from wordscore import score_word
    scores = []
    for word in valid_words:
        scores.append((score_word(word),word))
    scores = sorted(scores, key=lambda option: option[0], reverse=True)
    print(scores)
    
    return scores