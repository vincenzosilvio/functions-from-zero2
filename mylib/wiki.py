import wikipedia
from yake import KeywordExtractor


# build a function to return the summary of a wikipedia page
def get_wikipage(topic):
    """
    This function returns the summary of a wikipedia page
    :param topic: str
    :return: str
    """
    return wikipedia.summary(topic)


# build a function to search wikipedia pages for a match
def search_wikipedia(topic):
    """
    This function searches wikipedia pages for a match
    :param topic: str
    :return: list
    """
    return wikipedia.search(topic)


# return the keywords of a wikipedia page
def get_keywords(topic):
    """Get the top 10 keywords from a wikipedia page"""
    content = get_wikipage(topic)
    extractor = KeywordExtractor()
    keywords = extractor.extract_keywords(content)
    return {keyword: score for keyword, score in keywords[:10]}
