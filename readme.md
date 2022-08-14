# Machine Learning Project
Machine Learning course 2021-2022.<br>
Masters' Degree in Applied Mathematics, 
Sapienza University of Rome. <br>
Exam date: June 13th 2022


### Dataset and task description:
The provided [dataset](https://github.com/SofiaTorchia/Basic-analysis-of-MSFT-financial-data/blob/master/MSFT.csv)
consists of daily MSFT financial data from October 2013 to 
February 2022 [^1]. 
These data are initially pre-processed, then used to define some prediction models.
Given day $i$, consider the price of the stock in 
the following 10 days $i+1,...i+10$. <br>
Our target is to predict the highest price 
reached by MSFT stock in each of these 10 days, 
given information on day $i$. <br>
See this [notebook](https://github.com/SofiaTorchia/Basic-analysis-of-MSFT-financial-data/blob/master/Basic%20analysis%20of%20MSFT%20financial%20data.ipynb)
for detailed analysis and results.

### Feature engineering

Some fetures of the dataset are highly correlated 
to each other, and so redundant, since they don't 
provide the model with any additional useful 
information. <br>
However, new input features (technical indicators)
can be created from these correlated features. <br>
[Here](https://github.com/SofiaTorchia/Basic-analysis-of-MSFT-financial-data/blob/master/indicators.py)
the following indicators have been implemented:

1) Simple moving average.

2) MACD (Moving Average Convergence/Divergence). 

3) Average true range

4) Average typical price.

5) CCI (Commodity Channel Index)

### Model selection and evaluation
After feature selection and data transformation 
are performed, the following models are trained 
and evaluated by spitting the dataset for 
crossvalidation: 

- Linear regressor
- Multilayer perceptron
- Regression trees
- Random forest







<br/><br/>

[^1]: Data have been downloaded from https://www.marketwatch.com/investing/stock/msft/download-data.


