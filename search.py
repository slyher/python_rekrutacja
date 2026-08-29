import re


"""
This is the "search" module.

The search module supplies  function, search00x(word, sentence) whose responsibility is 
to return an list of indexes of every occurrence on an substring in a string.  
For example,

>>> search001('aa', 'makkaanada')
[4]

"""


def search001(word, sentence):
    """
    Return tha list of index of a substring found in string

    >>> search001('aa', 'makkaanada')
    [4]

    >>> search001('ad', 'makkaanada')
    [7]

    >>> search001('an', 'makkaanada')
    [5]
    """
    return [sentence.find(word)]


def search002(word, sentence):
    """
    Return tha list of indexs of a substring found in string

    >>> search002('aa', 'makkaanada')
    [4]

    >>> search002('ad', 'makkaanada')
    [7]

    >>> search002('an', 'makkaanada')
    [5]
    """
    return [re.search(word, sentence).span()[0]]


def search003(word: str, sentence: str) -> list:
    """
    Return tha list of indexs of a substring found in string

    >>> search003('aa', 'maakkaanaakka')
    [1, 5, 8]

    >>> search003('kk', 'maakkaanaakka')
    [3, 10]

    >>> search003('ak', 'maakkaanaakka')
    [2, 9]
    """
    return [match.start() for match in re.finditer(word, sentence)]


"""
plot twist the function has to be very fast 
- using str native functions in not an option
the response may be a generator
"""


def search004(word: str, sentence: str):
    """
    Return tha list of indexes of a substring found in string

    >>> search004('aa', 'maakkaanaakka')
    [1, 5, 8]

    >>> search004('kk', 'maakkaanaakka')
    [3, 10]

    >>> search004('ak', 'maakkaanaakka')
    [2, 9]
    """
    response = []
    word_len = len(word)
    for i in range(len(sentence) - word_len):
        if (word == sentence[i:i+word_len]):
            response.append(i)
    return response


def search005(word: str, sentence: str):
    """
    Return tha list of indexes of a substring found in string

    >>> list(search005('aa', 'maakkaanaakka'))
    [1, 5, 8]

    >>> list(search005('kk', 'maakkaanaakka'))
    [3, 10]

    >>> list(search005('ak', 'maakkaanaakka'))
    [2, 9]
    """
    word_len = len(word)
    for i in range(len(sentence) - word_len):
        if (word == sentence[i:i + word_len]):
            yield i


def search006(word: str, sentence: str):
    """
    Return a generator of indexes of a substring found in string

    >>> list(search006('aa', 'maakkaanaakka'))
    [1, 5, 8]

    >>> list(search006('kk', 'maakkaanaakka'))
    [3, 10]

    >>> list(search006('ak', 'maakkaanaakka'))
    [2, 9]

    >>> list(search006('au', 'maakkaanaakka'))
    []

    >>> list(search006('ana', 'maakkaanaakka'))
    [6]

    >>> list(search006('ana', 'maannakkaanaakka'))
    [9]

    """

    word_len = len(word)
    for i in range(len(sentence) - word_len):
        for j in range(word_len):
            if (sentence[i+j] == word[j]):
                if (j == word_len-1):
                    yield i
            else:
                break


if __name__ == "__main__":
    import doctest
    doctest.testmod()
