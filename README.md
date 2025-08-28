
#Time Series Decomposition & Forecasting

This repository provides a simple framework for time series analysis, decomposition, and forecasting using Python.
It includes utilities for reading data, plotting time series, decomposing into trend/seasonality/residuals, and forecasting.

#Features

##Data Reading

*read_data() in reading_data.py

Reads CSV data, parses a datetime column, and sets it as index.

##Visualization

*plot_time_series_data() in ts_plots.py

Plots time series with well-formatted date axis (Year-Month, quarterly ticks).

##Decomposition

*seasonality_decopositioin() for classical decomposition

*stl_decopose() for robust decomposition using STL (LOESS)

#Forecasting Workflow

1.Perform STL decomposition → separate trend, seasonality, and residuals.

2.Forecast trend and residuals using an ARIMA or another forecasting model.

3.Add back seasonality from the STL decomposition.

4.Get the final forecast = (forecasted (trend + residuals) + seasonality).