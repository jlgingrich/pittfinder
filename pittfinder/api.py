import requests
import pathlib

from selectolax.parser import HTMLParser


class APIError(BaseException):
    """Indicates that the API rejected a query."""


class TooManyResultsError(APIError):
    """Too many people matched your criteria. Please try searching by username, phone, email, or by enclosing your search in quotation marks."""


class AtSearchLimitError(APIError):
    """You have reached the search limit allowed. To continue, please wait 10 minutes or connect to the Pitt Network."""


DOMAIN = "https://find.pitt.edu"
SEARCH_ENDPOINT = DOMAIN + "/Search"
VCARD_ENDPOINT = DOMAIN + "/VCard/Index/{vcard_id}"

SESSION = requests.session()


# Low-level API
def get_search_response(query: str):
    """Performs the actual POST request and returns the raw response. Useful for debugging.

    Args:
        query (_type_): _description_

    Returns:
        _type_: _description_
    """
    return SESSION.post(SEARCH_ENDPOINT, data={"search": query, "layout": "list"})


def validate_search_response(html: str):
    """Validates a search response because the API returns errors in the HTML and not as HTTP status codes

    Args:
        html (str): The search response to validate

    Raises:
        TooManyResultsError: Too many people matched your criteria. Please try searching by username, phone, email, or by enclosing your search in quotation marks.
        AtSearchLimitError: You have reached the search limit allowed.  To continue, please wait 10 minutes or connect to the Pitt Network.
    """
    root = HTMLParser(html)
    # Check response for "too many search results" error
    error_message = root.css_first("div#searchResults div.content-alert")
    if error_message:
        raise TooManyResultsError(error_message.text(strip=True))
    # Check response for "search limit" error
    error_message = root.css_first("div#searchResults div.alert-warning")
    if error_message:
        raise AtSearchLimitError(error_message.text(strip=True))


def parse_search_response(html: str):
    """Parses the HTML returned from a search into a Python data structure

    Args:
        html (str): A string containing HTML data.

    Returns:
         list[dict[str, str | list[str]]]: A list of dictionaries containing user information
    """
    root = HTMLParser(html)
    users = []
    for tree in root.css("section.row div.col"):
        user_dict = {}
        # Most attributes can be scraped as key-value pairs
        for node in tree.css("div:not(:first-child)"):
            # Skip the more-info-link if encountered
            if node.attributes.get("class", "") == "more-info-link":
                continue
            k = node.css_first("span:first-child").text(strip=True)
            v = node.css_first("span:nth-of-type(2)").text(strip=True)
            # The html for this key isn't properly nested, so fix that
            if k == "Student Plan(s)":
                v = [v]
            if not k:
                user_dict["Student Plan(s)"].append(v)
            else:
                user_dict[k] = v
        # Hardcoded positions for these attributes
        user_dict["Name"] = tree.css_first(".person-header .title").text(strip=True)
        user_dict["Vcard ID"] = pathlib.PurePath(tree.css_first(".title .v-card").attributes["href"]).stem  # type: ignore
        users.append(user_dict)
    return users


def get_vcard_for_user(vcard_id: str):
    """Gets the contents of a VCARD for the given user

    Args:
        vcard_id (str): The given user's Vcard ID as returned by the API

    Returns:
        str: The content of the VCARD
    """
    return SESSION.get(VCARD_ENDPOINT.format(vcard_id=vcard_id)).text
