import numpy as np
import pandas as pd

def get_reg_line(X_train, y_train):
    """
    Compute linear regression predictions for the provided training data.

    Parameters
    ----------
    X_train : array-like or pd.DataFrame of shape (n_samples, n_features)
        The training input samples.
    y_train : array-like or pd.DataFrame of shape (n_samples,) or (n_samples, n_targets)
        The target values (real numbers).

    Returns
    -------
    y_pred : ndarray of shape (n_samples,) or (n_samples, n_targets)
        The predicted values calculated from the linear least-squares fit
    """
    X = np.asarray(X_train)
    y = np.asarray(y_train)

    # Add a column of ones to X to account for the intercept (bias) term
    X_bias = np.ones((X.shape[0], 1))

    # Create X_matrix of observations
    X_matrix  = np.concatenate((X_bias, X), axis=1)

    # Calculate the optimal weights (beta) using the Normal Equation
    # (X^T * X)^-1 * X^T * y
    beta = np.linalg.inv(X_matrix.T @ X_matrix) @ X_matrix.T @ y

    # Calculate predictions
    y_pred = X_matrix @ beta

    return y_pred