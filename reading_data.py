import pandas as pd
from datetime import datetime


def read_data(file_name, date="date", parser="%Y-%m-%d"):
    """
    Read a CSV file and parse a date column into a datetime index.

    Parameters
    ----------
    file_name : str
        Path to the CSV file.
    date : str, default="date"
        Column name containing the date values.
    parser : str, default="%Y-%m-%d"
        Datetime format string for parsing.

    Returns
    -------
    data : pandas.DataFrame
        DataFrame with datetime index.

    Examples
    --------
    >>> df = read_data("data.csv", date="date", parser="%Y-%m-%d")
    >>> df.head()
    """
    dateparse = lambda x: datetime.strptime(x, parser)
    data = pd.read_csv(file_name, parse_dates=[date], date_format=dateparse, index_col=date)
    return data
