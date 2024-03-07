"""Minimalist API for https://find.pitt.edu/"""

from .api import get_search_response, parse_search_response, validate_search_response


def search(query):
    """Wrapper around the <find.pitt.edu> search API.

    Args:
        query (str): The query to execute; searches most fields for each user.

    Raises:
        ValueError: If the query would return too many results.

    Returns:
        list[dict]: A list of user dictionaries with the returned information.
    """
    # Get raw response and attach HTML parser
    html = get_search_response(query).text
    # Check for and raise API errors
    validate_search_response(html)
    # Parse the returned html
    return parse_search_response(html)
