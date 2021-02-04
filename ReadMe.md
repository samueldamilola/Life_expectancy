## Project Overview
* Created a tool that estimated the life expectancy of 165 countries using the mean absolute error (MAE) and R squared (R2) for performance metrics. 
* Data used in for the project was provided by World Health Organization (W.H.O) in [kaggle link](https://www.kaggle.com/augustus0498/life-expectancy-who). Also, the second dataset that was merge with the first data can be obtained from [here](https://github.com/samueldamilola/Life_expectancy/blob/master/Region.csv).
* Model algorithm used were ordinary least square regression(OLS), multiple regression, lasso, support vector regressor, random forest regressor
* GridSearchCV was used to select the best performing model
* Built Flask API

## Motivation
Many factors has been noted to affect the life expectancy of countries. However, the significant of this factors not widely known. Therefore, looking extensively into these factors and how these factors can help have positive correlation and impact of life expectancy.

## Packages Used
**Python version:** 3.6<br>
**Packages:** Numpy, Pandas, matplotlib, seaborn, flask, pickle, json, requests<br> 
**Web Framework Requirement:** '''pip install -r requirements.txt'''<br>

## Data Cleaning
Check it out here [Data Cleaning](https://github.com/samueldamilola/Life_expectancy/blob/master/Data%20importation%20and%20cleaning.ipynb)

## Exploratory Data Analysis
* check out the relationship in our categorical features, I considered the following features: ['Status', 'Region', 'Income group']<br>
* Distributions of numerical variable  was looked into
Detail and well explained comments are here [EDA](https://github.com/samueldamilola/Life_expectancy/blob/master/Exploratory%20Data%20Analysis.ipynb)

## Model Performance
                          MAE            R2
**Multiple Regression:**    1.8063<span style="border-left:2px solid black;height:2px;margin-left:198px;padding-left:30px;">0.936<br>
**Support Vector Regressor:**       4.6823            0.407<br>
**Lasso:**                          2.0168            0.904<br>
**Random forest Regressor:**        2.0194            0.931<br>

* for details [Click here](https://github.com/samueldamilola/Life_expectancy/blob/master/Model%20Building.ipynb)

## Deployment
This deployment was used using Flask API
check it [here](https://github.com/samueldamilola/Life_expectancy/tree/master/Flask_API)

## Acknowledgement
I would like to acknowledge Kee Jee for providing massive support indirectly. Ideas gotten to build the regression project was from his videos on Data science projects for beginners. Thanks
