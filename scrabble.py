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
    
    # find valid words
    valid_words = [] # initialize an empty list to store all valid words
    #invalid_chars = []
    for word in sowpods_words:
        temp_rack = list(rack)
        temp_word = list(word)
        invalid_chars = []
        for letter in word:
            if letter in temp_rack:
                temp_rack.remove(letter)
                temp_word.remove(letter)
        if len(temp_word) - temp_rack.count('?') - temp_rack.count('*') <= 0:
            valid_words.append(word)
            invalid_chars.append(temp_word)

    # step 4 - scoring
    from wordscore import score_word
    score_list = []
    for word,wildcards in zip(valid_words,invalid_chars):
        score_list.append((score_word(word)-score_word(wildcards),word))
    score_list = sorted(score_list, key=lambda option: option[0], reverse=True)
    #score_list.append(len(score_list))
    valid_num = len(score_list)
    
    #print(f'This is finally returned -- \n{score_list}')
    
    #import sys
    #input_rack = sys.argv[1]
    #run_scrabble(input_rack)

    return score_list, valid_num