## Case Study - Churn Prediction

A one day group case-study to predict churn for a ride-sharing company. Audience was Marketing Team on the Driver Side.

###Problem Statement
A ride-sharing company (Company X) is interested in predicting rider retention. To help explore this question, We have a sample dataset of a cohort of users who signed up for an account in January 2014. The data was pulled on July 1, 2014; consider a user retained if they were “active” (i.e. took a trip) in the preceding 30 days (from the day the data was pulled). In other words, a user is "active" if they have taken a trip since June 1, 2014. The data are split into train and test sets. Tune and estimate the model's performance on the train set, then see how it does on the unseen data in the test set at the end.

Here is a detailed description of the data:

```
city: city this user signed up in
phone: primary device for this user
signup_date: date of account registration; in the form `YYYYMMDD`
last_trip_date: the last time this user completed a trip; in the form `YYYYMMDD`
avg_dist: the average distance (in miles) per trip taken in the first 30 days after signup
avg_rating_by_driver: the rider’s average rating over all of their trips
avg_rating_of_driver: the rider’s average rating of their drivers over all of their trips
surge_pct: the percent of trips taken with surge multiplier > 1
avg_surge: The average surge multiplier over all of this user’s trips
trips_in_first_30_days: the number of trips this user took in the first 30 days after signing up
luxury_car_user: TRUE if the user took a luxury car in their first 30 days; FALSE otherwise
weekday_pct: the percent of the user’s trips occurring during a weekday
```

## Objective
Use the data set to help understand what factors are the best predictors for retention, and offer suggestions to operationalize those insights to help Company X. Therefore, the task is not only to build a model that minimizes error, but also a model that allows us to interpret the factors that contributed to our predictions.

## Analysis
1. EDA - dummified the cities, for no ratings replaced with 0
2. Built a predictive model using Logistic Regression. Score of 0.68.
3. Important features rating_of_driver, surge_pct, weekday_pct.

## Actionable Plans
  Based on insights from the model,
  1. Churn in Winterfell is much lower than the other two cities.
  2. Driver ratings is much higher in Winterfell as well.
  3. We propose conducting a survey of drivers in Winterfell to find out what they are doing differently and duplicate the same for the other two cities.

Slides can be seen here:
https://docs.google.com/presentation/d/1MH__IAnZiHu7nUs0ujCS4b6axdLhgSSsIhA4y3j7drQ/edit#slide=id.gc6f9e470d_0_0
