from string_utils import is_full_string


def is_null_or_white_space(string: str):
    """
    Checks whether the string is null or an empty string.
    :returns: True if the string is null, an empty string or just whitespace. Otherwise, it returns false.
    """
    return not is_full_string(string)
