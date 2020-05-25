## Table of Contents

1. [Installation](#Installation)
2. [Description](#Description)
3. [Data](#Data)
4. [File Descriptions](#File-Descriptions)
5. [Results](#Results)
6. [Acknowledgements](#Acknowledgements)

## Installation
- Python 3.7.2
- Libraries: 
  - [Pandas](http://pandas.pydata.org)
  - [matplotlib](http://matplotlib.org/)
  - [seaborn](https://seaborn.pydata.org)
  - [statsmodels](https://www.statsmodels.org/stable/index.html)

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)

## Description

The business problem was formulated as follows:

> You recently started working for a company that manufactures and sells high-end home goods. 
> Last year the company sent out its first print catalog, and is preparing to send out this year's catalog 
> in the coming months. The company has 250 new customers from their mailing list that they want to send the catalog to. 
> Your manager has been asked to determine how much profit the company can expect from sending a catalog to these customers. 
> You, the business analyst, are assigned to help your manager run the numbers. While fairly knowledgeable about data analysis, 
> your manager is not very familiar with predictive models. 
> You’ve been asked to predict the expected profit from these 250 new customers.
> Management does not want to send the catalog out to these new customers unless the expected profit contribution exceeds $10,000. 

## Data 

`p1-customers.xlsx` - information on about 2,300 customers 

`p1-mailinglist.xlsx` - data on 250 customers that you need to predict sales


## File Descriptions

You can find the results of the analysis in either html form or complete Jupyter Notebook:

* [Predicting_Catalog_Demand.html](https://github.com/k-bosko/predicting_catalog_demand/blob/master/Predicting_Catalog_Demand.html)
* [Predicting_Catalog_Demand.ipynb](https://github.com/k-bosko/predicting_catalog_demand/blob/master/Predicting_Catalog_Demand.ipynb)

Alterinatively, run one the following commands in a terminal after navigating to the top-level project directory `predicting_catalog_demand/` (that contains this README):

```bash
ipython notebook Predicting_Catalog_Demand.ipynb
```  
or
```bash
jupyter notebook Predicting_Catalog_Demand.ipynb
```

This will open the iPython Notebook software and project file in your browser.

## Results

To predict catalog demand, I performed the following steps:

- **Step 1: Preprocessing**
  - explored datasets
  - split the data into target variable and features
  - checked for linear relationship between the target and numerical features using `sns.regplot()`
  - one-hot encoded categorical features using `pd.get_dummies()`

- **Step 2: Building Linear Regression Model**
  - checked for correlations between features to avoid multicollinearity using `corr()`
  - initialized and fit linear regression model with `sm.OLS()` from statsmodels library 
  - transformed the new customer data in the same way as the training set
  - scored the lm model on the new customer data, predicted the sales and calculated the possible profits

## Acknowledgements

Having started learning Python, I decided to rewrite the project I first completed in [Alteryx](https://www.alteryx.com)
within the [Predictive Analytics for Business Nanodegree at Udacity](https://www.udacity.com/course/predictive-analytics-for-business-nanodegree--nd008).
