"""Convenient helper functions for downloading responses."""

import json
import pathlib

from . import search
from .api import get_search_response, get_vcard_for_user


def download_raw_query_response(query: str):
    """Saves the raw query response to a local file for debugging purposes.

    Args:
        query (str): The query to return the response for
    """
    pathlib.Path(query.replace(" ", "_")).with_suffix(".html").write_text(
        get_search_response(query).text, encoding="utf-16"
    )


def download_query_response(query: str):
    """Simple way to save a query response to a local file

    Args:
        query (str): The query to return responses for
    """
    pathlib.Path(query.replace(" ", "_")).with_suffix(".json").write_text(
        json.dumps(search(query), indent=4, sort_keys=True), encoding="utf-16"
    )


def download_vcard(user_id: str, filepath: str = ""):
    """Saves a user's information as a VCARD file.

    Args:
        user_id (int): The ID of the user
        filepath (str | None, optional): The filepath to save the VCARD file to. Defaults to the ID.
    """
    pathlib.Path(filepath if filepath else user_id).with_suffix(".vcard").write_text(
        get_vcard_for_user(user_id), encoding="utf-16"
    )
