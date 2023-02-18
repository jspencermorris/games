
def score_word(word):
    """for a given word, return the score"""
    #! doesn't yet handle wildcards
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    scores = {k.upper():v for k,v in scores.items()}
    score = 0
    for char in word:
        score += scores[char]
    return score