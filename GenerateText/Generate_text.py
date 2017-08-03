import time
import numpy as np
from collections import Counter
from collections import defaultdict
import matplotlib.pyplot as plt


def unzip(pairs):
    """
    """
    return tuple(zip(*pairs))


def normalize(counter):
    """ 
    """
    total = sum(counter.values())
    return [(char, cnt / total) for char, cnt in counter.most_common()]


def train_lm(text, n):
    """ 
        Parameters
        -----------
        text: str 
            A string (doesn't need to be lowercased).
        n: int
            The length of n-gram to analyze.

        Returns
        -------
        A dict that maps histories (strings of length (n-1)) to lists of (char, prob) 
        pairs, where prob is the probability (i.e frequency) of char appearing after 
        that specific history. For example, if

    """
    raw_lm = defaultdict(Counter)
    history = "~" * (n - 1)

    # count number of times characters appear following different histories
    for x in text:
        raw_lm[history][x] += 1
        history = history[1:] + x

    # create final dictionary by normalizing
    lm = {history: normalize(counter) for history, counter in raw_lm.items()}

    return lm


def generate_letter(lm, history):
    """ 
        Parameters
        ----------
        lm: Dict[str, Tuple[str, float]] 
            The n-gram language model. I.e. the dictionary: history -> (char, freq)

        history: str
            A string of length (n-1) to use as context/history for generating 
            the next character.

        Returns
        -------
        str
            The predicted character. '~' if history is not in language model.
    """
    if not history in lm:
        return "~"
    letters, probs = unzip(lm[history])
    i = np.random.choice(letters, p=probs)
    return i


def generate_text(lm, n, nletters=100):
    """ 
        Parameters
        ----------
        lm: Dict[str, Tuple[str, float]] 
            The n-gram language model. I.e. the dictionary: history -> (char, freq)
        n: int
            Order of n-gram model.
        nletters: int
            Number of letters to randomly generate.

        Returns
        -------
        str
            Model-generated text.
    """
    history = "~" * (n - 1)
    text = []
    for i in range(nletters):
        c = generate_letter(lm, history)
        text.append(c)
        history = history[1:] + c
    return "".join(text)