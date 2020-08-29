

## Problem Formation: What additional features did you create? Please give a name and define each and why you felt it might help you.

- Feature #1: Weekend, 0 or 1 based on if it is a weekend, when the service is not available, I used this in my LSTM model.
- Feature #2: Weekday, Converting the DateTime to a value between 0-1 based on what the day of the week is, there are certain patterns that repeat on a weekly basis, would have used it in an LSTM model.
- Feature #3: Holiday, 1 if it is an observed holiday and 0 otherwise, this is important because if there is a holiday the next day will have a spike (given it is not a weekend), would have used it in an LSTM model.
- Feature #4: DJI,
- Feature #5: Lag, this is just taking the previous day, if one day is high, the next will be low, then high again. In addition, lag_7 (a week delay) had some of the best results, confirming my suspicion of every week being nearly the same. I used this in the ARIMA model but only with a one day lag.
## Concentration of Missing Data
![](https://camo.githubusercontent.com/1697eba4bb83e78c11dfd3745cb7fcd8c182e0e3/68747470733a2f2f6769746875622e636f6d2f6c656e6e796d656c6e696b2f70625f646174614368616c6c656e67652f7261772f6d61737465722f696d616765732f636f6e667573696f6e2e706e67)
## Skew and Distribution of Data
![](https://camo.githubusercontent.com/f720abde4454d768befb7586b883576656be7e72/68747470733a2f2f6769746875622e636f6d2f6c656e6e796d656c6e696b2f70625f646174614368616c6c656e67652f7261772f6d61737465722f696d616765732f70616972706c6f742e706e67)


## Feature Importance
![](https://camo.githubusercontent.com/e1850c88f0df52d4204fd6b3e4bfb7e89a5bad11/68747470733a2f2f6769746875622e636f6d2f6c656e6e796d656c6e696b2f70625f646174614368616c6c656e67652f7261772f6d61737465722f696d616765732f666561747572655f696d706f7274616e63652e6a706567)

## Algorithm Methods: What types of models did you use? Please give a name and define each and why you felt it might help you.

- Model Type #1: LSTM, Long-Short term memory which contains modules that lets it keep information over time, since we don't have much data of anomalies such as holidays, it is crucial to retain any information possible. In the end, I chose not to go with this model because it only gave me a 30% accuracy, which is not nearly good enough
- Model Type #2: ARIMA, a statistical method that isolates changes in data after removing trend and seasonality, it uses both regressions and moving average so it allows for a simple linear regression, after transforming the results it gave me the most accurate forecast.
## General Creativity and Explanation Explain the purpose of your model and how it might be used by a client (think of different reasons)

- The purpose of our model is to predict patterns in the number of returns and apply them to forecast future values. The ARIMA model is very flexible and a client could use it to predict the number of sales they would make in a given week. They could also use it to break down their information to understand the patterns that lie beneath constant growth and trends.
## Explain what your model does and how it works – how would you explain it to a non-technical person

- ARIMA predicts future values by assigning different importance weights to historical values, it also removes trend or seasonality. The way it does this is taking for example if we had 10 people of different heights. But instead of comparing everyone from shortest to tallest, we take the difference. So if the shortest person is 2 inches shorter than the next, the value we get is 2. It also values more recent events more.
## What challenges did you face in model development (technical, organizational, domain knowledge, etc…)

- We had never worked with ARIMA before, and it was definitely worth learning and understanding. Initially, we tried to transform the data before predicting. But since there were many 0's, a lot of transformation methods were out of the picture. When the model provided a prediction it had negative values, but that's not possible since there cannot be a negative amount of returns. Due to this, we had to transform the predictions, which I did not anticipate. 
### Before Transformation
![](https://camo.githubusercontent.com/babce485e6a567b5b33d34c12ea3c3f25af3bc49/68747470733a2f2f6769746875622e636f6d2f6c656e6e796d656c6e696b2f70625f646174614368616c6c656e67652f7261772f6d61737465722f696d616765732f6172696d615f6f726967696e616c5f70726564696374696f6e2e6a706567)


### After Transforming

![](https://camo.githubusercontent.com/c6e9ad2d0005e5167ec12723b6967cef235c272d/68747470733a2f2f6769746875622e636f6d2f6c656e6e796d656c6e696b2f70625f646174614368616c6c656e67652f7261772f6d61737465722f696d616765732f6172696d615f70726564696374696f6e2e706e67)

- Being sure that LSTM would work better it occupied the majority of the time. As soon as David provided the links for ARIMA I realized that it was the better solution.
- ARIMA is also mainly used with only one feature. In the future I would like to further develop it so that I may use a similar strategy, but with the other features that were available for use.
## What insights did you have from working on this project (not just the problem but the process)?

- Essentially correlation doesn't equal causation, for example, I had the Dow Jones Industrial average as a feature, and it showed a nearly 80 percent correlation. That just ended up being so because it too is closed on weekends. Yet again I am humbled by the amount of knowledge that is out there and how much there is to learn. Another thing is how much having like-minded people around you can help solve problems.
- The brain is like a muscle if you do not train it. It will get weak. Having not worked on Data Analytics in a couple of months it took me a while to get back into the flow of things. My teammates and I plan on practicing constantly (ex: Kaggle) to make sure that when we are given a problem, we know how to think properly to reach a solution
## What data would you request to provide a better estimate and why?

- The data we would request would be more specific to the facility. For example, the area in which it is located, as well as other details that differ from facility to facility. This would allow us to train the models better for individual facilities.
- Adding weather data would account for delays in returns and possibly allow for a more accurate forecast.
- In addition more data about anomalies such as holidays. So that we can train the model to associate any missing days, with the following being a spike.
- Finally, the number of packages delivered increased the number of returns. So being provided the merchant with consumer data could prove handy.