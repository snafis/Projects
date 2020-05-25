## Table of Contents

1. [Installation](#Installation)
2. [Description](#Description)
3. [Data](#Data)
4. [File Descriptions](#File-Descriptions)
5. [Results](#Results)
6. [Acknowledgements](#Acknowledgements)

## Installation
- Python 3.7.2
- _Libraries_: 
  - [NumPy](http://www.numpy.org/)
  - [Pandas](http://pandas.pydata.org)
  - [patsy](https://patsy.readthedocs.io/en/latest/)
  - [statsmodels](https://www.statsmodels.org/stable/index.html)
  - [matplotlib](http://matplotlib.org/)
  - [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)

## Description

The business problem was formulated as follows:
> Pawdacity is a leading pet store chain in Wyoming with 13 stores throughout the state. 
> This year, Pawdacity would like to expand and open a 14th store. Your manager has asked you 
> to perform an analysis to recommend the city for Pawdacity’s newest store, based on predicted yearly sales. 

## Data 

* `p2-2010-pawdacity-monthly-sales.csv` - This file contains all of the monthly sales for all Pawdacity stores for 2010.
* `p2-partially-parsed-wy-web-scrape.csv` - This is a partially parsed data file that can be used for population numbers.
* `p2-wy-453910-naics-data.csv` - NAICS data on the sales of all competitor stores where total sales is equal to 12 months of sales
* `p2-wy-demographic-data.csv` - This file contains demographic data for each city and county in Wyoming.

## File Descriptions

You can find the results of the analysis in either html form or complete Jupyter Notebook:

* [Pawdacity_New_Store_Location.html](https://github.com/k-bosko/new_store_location/blob/master/Pawdacity_New_Store_Location.html)
* [Pawdacity_New_Store_Location.ipynb](https://github.com/k-bosko/new_store_location/blob/master/Pawdacity_New_Store_Location.ipynb)

Alterinatively, run one the following commands in a terminal after navigating to the top-level project directory `new_store_location` (that contains this README):

```bash
ipython notebook Pawdacity_New_Store_Location.ipynb
```  
or
```bash
jupyter notebook Pawdacity_New_Store_Location.ipynb
```

This will open the iPython Notebook software and project file in your browser.

## Results

To identify the new city location based on potential sales, I performed the following steps:

- **Step 1: Preprocessing**
  - aggregated sales data from months to years
  - cleaned and joined census data with sales data and demographics data
  - dealt with outliers
  
- **Step 2: Predictive Modeling**
  - checked for `corr()` between  predictor variables to avoid multicollinearity
  - removed certain features based on their `variance_inflation_factor()`
  - calculated `OLS()` Regression and removed not statistically significant predictors
  - predicted sales for new cities with the final linear regression model
  - filtered data according to provided criteria for the new city
  
## Acknowledgements

Having started learning Python, I decided to rewrite the project I first completed in [Alteryx](https://www.alteryx.com)
within the [Predictive Analytics for Business Nanodegree at Udacity](https://www.udacity.com/course/predictive-analytics-for-business-nanodegree--nd008).
