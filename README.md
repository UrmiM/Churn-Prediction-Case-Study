## Case Study - Churn Prediction

A one day group case-study to predict churn for a ride-sharing company. Audience was Marketing Team on the Driver Side.

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

## Analysis
1. EDA - dummified the cities, for no ratings replaced with 0
2. Built a predictive model using Logistic Regression. Score of 0.68.
3. Important features rating_of_driver, surge_pct, weekday_pct.


## Actionable Plans
  Based on insights from the model,
  1. Churn in Winterfell is much lower than the other two cities.
  2. Driver ratings is much higher in Winterfell as well.
  3. We propose conducting a survey of drivers in Winterfell to find out what they are doing differently and duplicate the same for the other two cities.
