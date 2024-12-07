import numpy as np;

# Define a class called Linear_Regression
class Linear_Regression:

    # initialize the class
    def __init__(self):
        self.coefficients = None;
        self.intercept = None;

    # fit the model
    def fit(self, X, y):
        # adding intercept to the input data
        X = np.c_[np.ones(X.shape[0]), X];
        # calculate the coefficients
        self.coefficients = np.linalg.inv(X.T @ X) @ X.T @ y;
        # set the intercept
        self.intercept = self.coefficients[0];
        # set the coefficients
        self.coefficients = self.coefficients[1:];

    # predict the values
    def predict(self, X):
        # adding intercept to the input data
        X = np.c_[np.ones(X.shape[0]), X];
        # calculate the predictions
        return X @ np.r_[self.intercept, self.coefficients];

    


