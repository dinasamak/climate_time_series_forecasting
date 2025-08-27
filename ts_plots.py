import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates


def plot_time_series_data(df, col, date='date'):
    """
    Plot a time series column with formatted date axis.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing a datetime index and a target column.
    col : str
        Column name to plot.
    date : str, default='date'
        (Optional) Name of the date column, if relevant.

    Returns
    -------
    None
        Displays a matplotlib plot.

    Examples
    --------
    >>> plot_time_series_data(df, 'sales')
    """
    x = df.index.to_numpy()
    y = df[col].to_numpy()

    fig, ax = plt.subplots(figsize=(30, 6))
    ax.plot(x, y, label=col)

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))  # Year-Month
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # every 3 months

    plt.xlabel("Date")
    plt.ylabel(col)
    plt.title(f"Time Series of {col}")
    plt.legend()
    plt.grid(True)
    plt.show()
