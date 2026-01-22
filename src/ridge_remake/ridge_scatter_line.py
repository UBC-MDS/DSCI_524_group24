import numpy as np


def ridge_scatter_line(ax, x, y_line, *, line_kwargs=None, label=None, sort_x=True):
    """
    Overlay a precomputed regression line on an existing scatter plot.

    This function does NOT fit a model. It takes the x-values used in the scatter
    plot and a matching set of precomputed y-values (for example, predictions
    returned by get_reg_line), then draws the line on the provided Matplotlib Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes on which to draw the regression line. Typically the same axes
        returned by ridge_scatter().
    x : array-like of shape (n_samples,)
        X-coordinates corresponding to the predictions in y_line.
    y_line : array-like of shape (n_samples,)
        Precomputed y-values to plot as a line (e.g., regression predictions).
        Must be the same length as x.
    line_kwargs : dict, optional
        Keyword arguments forwarded to Matplotlib's plot() to style the line
        (e.g., {"linewidth": 2, "linestyle": "--"}). If None, defaults are used.
    label : str, optional
        Legend label for the regression line.
    sort_x : bool, optional
        If True (default), sort points by x before plotting so the line does not
        zig-zag when x is not already ordered.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The same axes, with the regression line added.
    line : matplotlib.lines.Line2D
        The line artist created by Matplotlib.

    Raises
    ------
    TypeError
        If ax is not Axes-like, if line_kwargs is not a dict/None, if label is not
        a string/None, if sort_x is not boolean, or if inputs cannot be converted
        to numeric arrays.
    ValueError
        If x or y_line are empty, or if they have different lengths.
    """
    if ax is None or not hasattr(ax, "plot"):
        raise TypeError("ax must be a Matplotlib Axes-like object with a .plot method.")

    if line_kwargs is None:
        line_kwargs = {}
    elif not isinstance(line_kwargs, dict):
        raise TypeError("line_kwargs must be a dict or None.")

    if label is not None and not isinstance(label, str):
        raise TypeError("label must be a string or None.")

    if not isinstance(sort_x, (bool, np.bool_)):
        raise TypeError("sort_x must be a boolean.")

    try:
        x_arr = np.asarray(x, dtype=float).ravel()
        y_arr = np.asarray(y_line, dtype=float).ravel()
    except (TypeError, ValueError):
        raise TypeError("x and y_line must be numeric array-like inputs.") from None

    if x_arr.size == 0 or y_arr.size == 0:
        raise ValueError("x and y_line must be non-empty.")

    if x_arr.size != y_arr.size:
        raise ValueError("x and y_line must be the same length.")

    if sort_x:
        order = np.argsort(x_arr)
        x_arr = x_arr[order]
        y_arr = y_arr[order]

    (line,) = ax.plot(x_arr, y_arr, label=label, **line_kwargs)
    return ax, line
