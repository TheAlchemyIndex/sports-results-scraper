def extract_date_time(date_string: str, string_splitter: str) -> list[str]:
    """Takes a string, removes bracket based characters and splits it by a specified character string to return
    a list[str] of a date and time.

    :rtype: list[str]
    :param date_string: Original date string that contains bracket based characters and a unique character
    string
    :param string_splitter: Unique character string that the date string will be split using
    :return: list[str] containing a date and a time
    """
    # Splits the date by a specified character string (string_splitter)
    date_string_split: list[str] = date_string.split(string_splitter)

    # If the split was not successful, an N/A string is added as second element in date_string_split list
    if len(date_string_split) == 1:
        date_string_split.append("N/A")

    return date_string_split
