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
  - [matplotlib](http://matplotlib.org/)
  - [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)

## Description

CharityML is a fictitious charity organization located in the heart of Silicon Valley that was established to provide financial support for people eager to learn machine learning. After nearly 32,000 letters were sent to people in the community, CharityML determined that every donation they received came from someone that was making more than $50,000 annually. To expand their potential donor base, CharityML has decided to send letters to residents of California, but to only those most likely to donate to the charity. The goal is to evaluate and optimize several different supervised learners to determine which algorithm will provide the highest donation yield while also reducing the total number of letters being sent.

## Data 
The modified census dataset consists of approximately 32,000 data points, with each datapoint having 13 features. This dataset is a modified version of the dataset published in the paper *["Scaling Up the Accuracy of Naive-Bayes Classifiers: a Decision-Tree Hybrid",* by Ron Kohavi](https://www.aaai.org/Papers/KDD/1996/KDD96-033.pdf). 

**Features**
- `age`: Age
- `workclass`: Working Class (Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked)
- `education_level`: Level of Education (Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool)
- `education-num`: Number of educational years completed
- `marital-status`: Marital status (Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse)
- `occupation`: Work Occupation (Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces)
- `relationship`: Relationship Status (Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried)
- `race`: Race (White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black)
- `sex`: Sex (Female, Male)
- `capital-gain`: Monetary Capital Gains
- `capital-loss`: Monetary Capital Losses
- `hours-per-week`: Average Hours Per Week Worked
- `native-country`: Native Country (United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands)

**Target Variable**
- `income`: Income Class (<=50K, >50K)

## File Descriptions

You can find the results of the analysis in either html form or complete Jupyter Notebook:

* [finding_donors.html](https://github.com/k-bosko/finding_donors/blob/master/finding_donors.html)
* [finding_donors.ipynb](https://github.com/k-bosko/finding_donors/blob/master/finding_donors.ipynb)

Alterinatively, run one the following commands in a terminal after navigating to the top-level project directory `finding_donors/` (that contains this README):

```bash
ipython notebook finding_donors.ipynb
```  
or
```bash
jupyter notebook finding_donors.ipynb
```

This will open the iPython Notebook software and project file in your browser.

## Results

To identify the most promising donators based on their income I performed the following steps:

- **Step 1: Preprocessing**
  - plotted histograms of the two highly skewed continuous features
  - applied _logarithmic transformation_ on them
  - normalized numerical features using `MinMaxScaler()`
  - one-hot encoded categorical variables with `pd.get_dummies()`
  - split the data into training (80%) and test sets (20%) with `train_test_split()` function
  
- **Step 2: Creating a Training and Predicting Pipeline**
  - created `train_predict()` function that does the following:
    - fits the learner to the sampled training data and records the training time
    - performs predictions on the test data `X_test`, and also on the first 300 training points `X_train[:300]`
    - records the total prediction time
    - calculates the `accuracy_score()` and `fbeta_score()` for both the training subset and testing set.
  - applied the `train_predict()` function ob the three supervised learning models:
    - `RandomForestClassifier()`
    - `AdaBoostClassifier()`
    - `GradientBoostingClassifier()`
    
- **Step 3: Improving Results**
   - performed a grid search optimization via `GridSearchCV()` for two parameters `n_estimators` and `learning_rate`
   - made predictions using the unoptimized and optimized model
   - compared the before-and-after scores (accuracy and F-score) on the testing data 
   
- **Step 4: Extracting Feature Importance**
   - determined the top5 most predictive features using `feature_importances_` attribute

## Acknowledgements
The project is part of the [Udacity Data Science Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025). 

The dataset for this project originates from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Census+Income). The dataset was donated by Ron Kohavi and Barry Becker, after being published in the article _"Scaling Up the Accuracy of Naive-Bayes Classifiers: A Decision-Tree Hybrid"_. You can find the article by Ron Kohavi [online](https://www.aaai.org/Papers/KDD/1996/KDD96-033.pdf). 
