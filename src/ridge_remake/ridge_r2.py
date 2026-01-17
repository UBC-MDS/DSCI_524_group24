import numpy as np

def ridge_get_r2(y_true, y_pred):
    """
    Calculate the coefficient of determination (R² score) for a regression model.
    
    The R² score measures how well the regression line fits the data, representing
    the proportion of variance in the dependent variable that is predictable from
    the independent variable(s). Values range from -∞ to 1, where 1 indicates
    perfect prediction.

    This function calcuates the ratio of the Residual Sum of Squares (RSS) to the
    Total Sum of Squares (TSS), as a measure of how well the data performs compared
    to the mean.
    
    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True target values (observed data points).
    y_pred : array-like of shape (n_samples,)
        Predicted values from the regression model.
    
    Returns
    -------
    r2 : float
        The R² score. A value of 1.0 indicates perfect prediction, 0.0 indicates
        the model performs no better than predicting the mean, and negative values
        indicate the model performs worse than a horizontal line at the mean.
    
    Notes
    -----
    R² is calculated as:
        R² = 1 - (SS_res / SS_tot)
    where:
        SS_res = Σ(y_true - y_pred)²  (residual sum of squares)
        SS_tot = Σ(y_true - ȳ)²       (total sum of squares)
    
    Examples
    --------
    >>> y_true = np.array([3, -0.5, 2, 7])
    >>> y_pred = np.array([2.5, 0.0, 2, 8])
    >>> ridge_get_r2(y_true, y_pred)
    0.9486081370449679
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if not isinstance(y_true, (list, np.ndarray, tuple)) or \
       not isinstance(y_pred, (list, np.ndarray, tuple)):
        raise TypeError("y_true and y_pred must be array-like (list, tuple, or numpy array).")

    if y_true.ndim == 0 or y_pred.ndim == 0:
        raise TypeError("Input cannot be a single scalar value. Must be a sequence.")

    if y_true.size == 0 or y_pred.size == 0:
        raise ValueError("Input arrays cannot be empty.")

    if y_true.shape != y_pred.shape:
        raise ValueError(f"Shape mismatch: y_true {y_true.shape} vs y_pred {y_pred.shape}.")

    ss_res = np.sum((y_true - y_pred) ** 2)
    y_mean = np.mean(y_true)
    ss_tot = np.sum((y_true - y_mean) ** 2)

    if ss_tot == 0:
        return 1.0 if ss_res == 0 else 0.0

    r2 = 1 - (ss_res / ss_tot)
    return float(r2)