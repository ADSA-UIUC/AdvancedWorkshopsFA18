# -*- coding: utf-8 -*-
"""
As part of the UIUC Association of Data Science and Analytics Advanced Workshop Series - Intro to Supervised Learning Session.

Presented and developed by Sarah Khan, Rohan Tikmany, and Bailey Tincher on September 16th, 2018.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)
from mpl_toolkits.mplot3d import Axes3D


class gradient_descent_linear_regression:
  """cost function to compute the error in our model

  features - numpy matrix of all X variables
  targets - numpy matrix of all Y variables
  coefficients - numpy matrix of the weights of each Xi in X
  return - the cost (error) in our model as a floating point value
  """
  def _cost(features, targets, coefficients):
    hypothesis = features.dot(coefficients)
    loss = hypothesis - targets
    num_rows = len(targets)
    cost = np.sum(loss ** 2) / (2 * num_rows)
    return cost

  """training model for gradient descent multivariate linear regression

  features - numpy matrix of all X variables
  targets - numpy matrix of all Y variables
  coefficients - numpy matrix of the weights of each Xi in X
  learning_rate - the gradient descent step size
  iterations - the number of times the model recalculates its coefficients
  return - the final coefficients as an array
  return - an array of costs from each iteration
  """
  def train(features, targets, coefficients, learning_rate = .0001, iterations = 100000):
    cost_history = # Initialize list of size iterations to all 0's
    num_rows = # Compute number of data points
    
    for iteration in range(iterations):
      hypothesis = # Compute the predicted target values as a matrix
      loss = # Compute the difference between hypothesis (predicted) and target (actual) values in the matrices
      
      gradient = # Compute the new gradient for this iteration as a float
      coefficients = # Compute the new coefficients as a matrix from the new gradient
      
      cost = # Calculate the cost from this iteration

      cost_history[iteration] = cost # Store the cost in the history
      
    return coefficients, cost_history

  """Tests the accuracy of our model (use different data than train)

  features - the test data features
  targets - the actual values from test data
  coefficients - the final coefficients from our model as an array
  return - root mean square error as a float - lower is better
  return - R^2 accuracy score (0.0-1.0) - higher is better
  """
  def test(features, targets, coefficients):
    predictions = features.dot(coefficients)
    
    # Compute root mean square error of model
    diff = targets - predictions
    num_rows = len(targets)
    
    rmse = np.sqrt(sum(diff ** 2) / num_rows)
    
    # Compute R^2 score of model
    mean_targets = np.mean(targets)
    sq_diff_from_mean = sum((targets - mean_targets) ** 2)
    sq_diff_from_pred = sum((targets - predictions) ** 2)
    
    R2_accuracy = 1 - (sq_diff_from_pred / sq_diff_from_mean)
    
    return rmse, R2_accuracy

data = pd.read_csv("student.csv")

# Ploting the scores as scatter plot
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data['Math'].values, data['Reading'].values, data['Writing'].values, color='#ef1234', label='Scatter Plot')
ax.set_xlabel('Math score (%)')
ax.set_ylabel('Reading score (%)')
ax.set_zlabel('Writing score (%)')
plt.title("Reading and Math vs. Writing Scores Data")
plt.legend()
plt.show()

train_data = data.head(700)

math_train = train_data['Math'].values
read_train = train_data['Reading'].values
write_train = train_data['Writing'].values

intercepts = np.ones(len(math_train))
features = np.array([intercepts, math_train, read_train]).T
targets = np.array(write_train)
coefficients = np.array([0, 0, 0])

new_coefficients, cost_history = gradient_descent_linear_regression.train(features, targets, coefficients)

z_int = new_coefficients[0]
slope_x = new_coefficients[1]
slope_y = new_coefficients[2]

print("z-intercept: {0}, x_slope: {1}, y_slope: {2}".format(z_int, slope_x, slope_y))

print("The cost per 10,000 iterations is: {0}".format(cost_history[::10000]))

# Ploting Values and Regression Line
max_x = np.max(data['Math'].values)
min_x = np.min(data['Math'].values) - 5

max_y = np.max(data['Reading'].values)
min_y = np.min(data['Reading'].values) - 5

# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = np.linspace(min_y, max_y, 1000)
z = z_int + slope_x * x + slope_y * y

# Ploting Line

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data['Math'].values, data['Reading'].values, data['Writing'].values, color='#ef1234', label='Scatter Plot')
ax.plot(x, y, z, color='#58b970', label='Regression Line')
ax.set_xlabel('Math score (%)')
ax.set_ylabel('Reading score (%)')
ax.set_zlabel('Writing score (%)')
plt.title("Reading and Math vs. Writing Scores Data")
plt.legend()
plt.show()

test_data = data.tail(300)

math_test = test_data['Math'].values
read_test = test_data['Reading'].values
write_test = test_data['Writing'].values

test_intercepts = np.ones(len(math_test))
test_features = np.array([test_intercepts, math_test, read_test]).T
test_targets = np.array(write_test)


rmse, R2_score = gradient_descent_linear_regression.test(test_features, test_targets, new_coefficients)
print("Root Mean Square Error (RMSE): {0}, R^2 Score: {1}".format(rmse, R2_score))