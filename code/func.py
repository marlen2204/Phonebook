import json


def load_queries(filename: str) -> dict:
    """
    This is a function for reading sql queries
    :param filename:
    :return queries:
    """

    with open(filename, 'r', encoding='utf-8') as f:
        queries = json.load(f)
    return queries
