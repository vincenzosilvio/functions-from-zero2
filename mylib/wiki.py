import wikipedia

#build a function to return the summary of a wikipedia page
def get_summary(topic):
    """
    This function returns the summary of a wikipedia page
    :param topic: str
    :return: str
    """
    return wikipedia.summary(topic)

#build a function to search wikipedia pages for a match
def search_wikipedia(topic):
    """
    This function searches wikipedia pages for a match
    :param topic: str
    :return: list
    """
    return wikipedia.search(topic)

