import numpy as np

def ridge_scatter(ax, x, y, *, scatter_kwargs=None, label=None):
    """
    Create a scatter plot on a provided Matplotlib Axes object.

    This function is the base plotting function for the ridge regression
    visualization workflow. It draws the raw data points (x, y) on the provided
    Axes. A separate function, ``ridge_scatter_line()``, can then be called to
    overlay a precomputed regression line on the same Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes on which to draw the scatter plot.
    x : array-like of shape (n_samples,)
        X-coordinates of the data points.
    y : array-like of shape (n_samples,)
        Y-coordinates of the data points. Must be the same length as x.
    scatter_kwargs : dict, optional
        Keyword arguments forwarded to Matplotlib's scatter() to style the points
        (e.g., {"s": 25, "alpha": 0.8, "marker": "o"}). If None, defaults are used.
    label : str, optional
        Legend label for the scatter points.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The same axes, with the scatter points added.
    points : matplotlib.collections.PathCollection
        The scatter artist created by Matplotlib.

    Notes
    -----
    This function only creates the scatter plot and does not compute or overlay any
    fitted line. To overlay a precomputed line after plotting points, call
    ``ridge_scatter_line(ax, x_line, y_line, ...)``.
    """
    if ax is None or not hasattr(ax, "scatter"):
        raise TypeError("ax must be a Matplotlib Axes-like object with a .scatter method.")

    if scatter_kwargs is None:
        scatter_kwargs = {}
    elif not isinstance(scatter_kwargs, dict):
        raise TypeError("scatter_kwargs must be a dict or None.")

    if label is not None and not isinstance(label, str):
        raise TypeError("label must be a string or None.")

    try:
        x_arr = np.asarray(x, dtype=float).ravel()
        y_arr = np.asarray(y, dtype=float).ravel()
    except (TypeError, ValueError):
        raise TypeError("x and y must be numeric array-like inputs.") from None

    if x_arr.size == 0 or y_arr.size == 0:
        raise ValueError("x and y must be non-empty.")

    if x_arr.size != y_arr.size:
        raise ValueError("x and y must be the same length.")

    points = ax.scatter(x_arr, y_arr, label=label, **scatter_kwargs)
    return ax, points