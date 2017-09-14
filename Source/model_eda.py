from eda import *


from sklearn.linear_model import LogisticRegression
from statsmodels.tools import add_constant

df = df.dropna()

test = pd.read_csv('data/churn_test.csv')
test = test.dropna()

test['last_trip_date'] = pd.to_datetime(test['last_trip_date'])
test['signup_date'] = pd.to_datetime(test['signup_date'])
today = df.last_trip_date.max()
test['Churn']= test['last_trip_date'].apply(lambda x : 1 if today-x> timedelta(days=30) else 0)

model1_data = df[['avg_rating_of_driver', 'avg_surge', 'trips_in_first_30_days', 'Churn']]
model2_data = df[['avg_dist', 'avg_rating_of_driver', 'avg_surge', 'trips_in_first_30_days', 'Churn']]

y = model1_data['Churn'].values

# df['last_trip_date'] = df.last_trip_date.astype(int)
# df['signup_date'] = df.last_trip_date.astype(int)

# X = df.drop('Churn', 1).values
X = model1_data[['avg_rating_of_driver', 'avg_surge', 'trips_in_first_30_days']].values
X_const = add_constant(X, prepend=True)

# data for model 2
X2 = model2_data[['avg_dist', 'avg_rating_of_driver', 'avg_surge', 'trips_in_first_30_days']].values
y2 = model2_data[['Churn']].values

y_test = test['Churn']
X_test = test[['avg_rating_of_driver', 'avg_surge', 'trips_in_first_30_days', 'avg_dist']].values

#first model
logit_model = LogisticRegression()
logit_model.fit(X, y)

#second model
logit_model2 = LogisticRegression()
logit_model2.fit(X2, y2)

print logit_model2.score(X_test, y_test)
