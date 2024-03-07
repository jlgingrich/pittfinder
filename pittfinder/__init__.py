"""Minimalist API for https://find.pitt.edu/"""

import pittfinder.api as _api


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
    html = _api.get_search_response(query).text
    # Check for and raise API errors
    _api.validate_search_response(html)
    # Parse the returned html
    return _api.parse_search_response(html)
