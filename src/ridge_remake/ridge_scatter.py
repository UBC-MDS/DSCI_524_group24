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
    pass