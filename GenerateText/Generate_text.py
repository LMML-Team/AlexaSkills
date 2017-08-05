import time
import numpy as np
from collections import Counter
from collections import defaultdict
import matplotlib.pyplot as plt


def unzip(pairs):
    """
    Splits list of pairs (tuples) into separate lists
    
    Parameter(s)
    --------------
    pairs(list of tuples):
        List of pairs to be split
    
    Return(s)
    --------------
    list 1:
        List containing the first term of all pairs
        
    list 2:
        List containing the second term of all pairs
        
    Example(s)
    --------------
    
    pairs = [("a", 1), ("b", 2)] --> ["a", "b"] and [1, 2]
        
    """
    return tuple(zip(*pairs))


def normalize(counter):
    """ 
    Convert counter to a list of (letter, frequency) pairs, sorted in descending order of frequency
    
    Parameter(s)
    --------------
    counter (Counter-instance):
        Counter to be converted. Letters and their # of occurrences
        
    Return(s)
    --------------
    list[tuples]:
        List containing tuples of (letter, frequency) pairs
        
    Example(s)
    --------------
        counter = Counter({'a': 1, 'b': 3})
        normalize(counter) = [('b', 0.75), ('a', 0.25)]
    
    """
    total = sum(counter.values())
    return [(char, cnt / total) for char, cnt in counter.most_common()]


def train_lm(text, n):
    """ 
    Train character-based n-gram language model.
    Given a sequence of n-1 characters, what is the probability distribution
    for the n-th character in the sequence.
    
    Parameter(s)
    --------------
    text(str):
        A string (any case)
        
    n(int):
        Order of n-gram model

    Returns
    --------------
    dict({ strings of len n-1: list[(char, probability)]:
        Maps histories of characters (led by ~ if # of proceeding chars < n-1)
        to list of pairs containing chars and the probability of them appearing
        after that particular history
    
    Example(s)
    --------------
    text = "cacao"
    n = 3
    train_lm(text, n) ={'ac': [('a', 1.0)],
                        'ca': [('c', 0.5), ('o', 0.5)],
                        '~c': [('a', 1.0)],
                        '~~': [('c', 1.0)]}

    """
    # Initialize lm and history
    raw_lm = defaultdict(Counter)
    history = "~" * (n - 1)

    # Count number of times characters appear following different histories
    for x in text:
        raw_lm[history][x] += 1
        history = history[1:] + x

    # Create final dictionary by normalizing
    lm = {history: normalize(counter) for history, counter in raw_lm.items()}

    return lm


def generate_letter(lm, history):
    """ 
    Generates a letter according to the probability distribution of the specified history
    
    Parameter(s)
    --------------
    lm (Dict{str: Tuple(str, float)}):
        The n-gram language model relating history to letter probabilities

    history (str):
        Length n-1 context for use as key in language model

    Returns
    --------------
    str:
        The predicted character. '~' if history is not in language model.
    """

    # Default behaviour if history is not in the model
    if not history in lm:
        return "~"

    # Uses unzip function to split the letters from their probabilities
    letters_probs = unzip(lm[history])

    # Randomly selects and returns a letter from letters with its p in probs
    i = np.random.choice(letters_probs[0], p=letters_probs[1])
    return i


def generate_text(lm, n, nletters=100):
    """ 
    Generates nletters random letters according to n-gram language model, lm
    
    Parameters
    --------------
    lm (Dict{str: Tuple(str, float)}):
        The n-gram language model relating history to letter probabilities
        
    n (int):
        Order of n-gram model.
        
    nletters: int
        Number of letters to randomly generate.

    Returns
     --------------
    str
        Model-generated text.
    """

    # Initializes history and text
    text = []
    history_indices = np.arange(len(lm.keys()))
    index = np.random.choice(history_indices)
    history = lm[index]


    # uses generate_letter function to generate text that is nletters long
    for i in range(nletters):
        c = generate_letter(lm, history)
        text.append(c)
        history = history[1:] + c

    # Joins and returns the characters in text
    return "".join(text)