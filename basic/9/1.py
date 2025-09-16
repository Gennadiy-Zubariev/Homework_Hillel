def popular_words(text: str, words: list) -> dict:
    """
    The function counts the number of occurrences of words in a string.

    :param text: String where words are searched
    :param words: List of words to search for
    :return: Dictionary with the number of occurrences of a word in a term
    """
    res = {}
    for word in words:
        res[word] = text.lower().split().count(word)
    return res


assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new ''',
    ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0,
                                       'near': 0}, 'Test1'
print('OK')
