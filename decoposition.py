import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.seasonal import STL
import matplotlib.pyplot as plt


def seasonality_decopositioin(df, period=12, plot=False):
    """
    Perform classical seasonal decomposition using moving averages.

    Parameters
    ----------
    df : pandas.Series or pandas.DataFrame
        Time series data (must have a datetime index).
    period : int, default=12
        Number of periods in a season (e.g., 12 for monthly data with yearly seasonality).
    plot : bool, default=False
        If True, plots observed, trend, seasonal, and residual components.

    Returns
    -------
    result : statsmodels.tsa.seasonal.DecomposeResult
        Decomposition results containing observed, trend, seasonal, and resid components.

    Examples
    --------
    >>> result = seasonality_decopositioin(df['sales'], period=12, plot=True)
    >>> result.seasonal.head()
    """
    result = seasonal_decompose(df, model='additive', period=period)
    
    if plot:
        fig, axes = plt.subplots(4, 1, figsize=(12, 8), sharex=True)
        result.observed.plot(ax=axes[0], legend=False, title="Observed")
        result.trend.plot(ax=axes[1], legend=False, title="Trend")
        result.seasonal.plot(ax=axes[2], legend=False, title="Seasonal")
        result.resid.plot(ax=axes[3], legend=False, title="Residual")
        plt.tight_layout()
        plt.show()

    return result


def stl_decopose(df, period=12, plot=False):
    """
    Perform seasonal-trend decomposition using LOESS (STL).

    Parameters
    ----------
    df : pandas.Series or pandas.DataFrame
        Time series data (must have a datetime index).
    period : int, default=12
        Number of periods in a season.
    plot : bool, default=False
        If True, plots observed, trend, seasonal, and residual components.

    Returns
    -------
    result : statsmodels.tsa.seasonal.STLResult
        Decomposition results containing observed, trend, seasonal, and resid components.

    Examples
    --------
    >>> result = stl_decopose(df['sales'], period=12, plot=True)
    >>> result.trend.head()
    """
    stl = STL(df, period=period)
    result = stl.fit()
    
    if plot:
        fig, axes = plt.subplots(4, 1, figsize=(12, 8), sharex=True)
        result.observed.plot(ax=axes[0], legend=False, title="Observed")
        result.trend.plot(ax=axes[1], legend=False, title="Trend")
        result.seasonal.plot(ax=axes[2], legend=False, title="Seasonal")
        result.resid.plot(ax=axes[3], legend=False, title="Residual")
        plt.tight_layout()
        plt.show()

    return result
