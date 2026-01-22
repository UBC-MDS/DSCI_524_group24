
import matplotlib
import numpy as np
import pytest

matplotlib.use("Agg")  
import matplotlib.pyplot as plt

from ridge_remake.ridge_scatter import ridge_scatter
from ridge_remake.ridge_scatter_line import ridge_scatter_line

"""
PROMPT FOR CHATGPT:
Write pytest unit tests for ridge_scatter_line.

Create test functions for these cases

Cover:
(1) normal overlay adds exactly 1 line to ax and line x/y match expected (sorted by x by default),
(2) sort_x=False keeps original x order,
(3) invalid ax (None or no .plot) -> TypeError,
(4) x and y_line length mismatch -> ValueError,
(5) non-numeric x or y_line -> TypeError,
(6) line_kwargs not dict/None -> TypeError.
"""


def test_overlay_line_sorted_by_x():
    """Line should be sorted by x by default so it doesn't zig-zag."""
    fig, ax = plt.subplots()

    x = np.array([3, 1, 2])
    y = np.array([30, 10, 20])
    y_line = np.array([6, 2, 4])  # y = 2x

    ridge_scatter(ax, x, y)
    ridge_scatter_line(ax, x, y_line, label="fit")

    assert len(ax.collections) == 1, "Expected one scatter plot collection on the axes."
    assert len(ax.lines) == 1, "Expected one line to be added to the axes."

    line = ax.lines[0]
    np.testing.assert_allclose(line.get_xdata(), np.array([1, 2, 3]))
    np.testing.assert_allclose(line.get_ydata(), np.array([2, 4, 6]))

    plt.close(fig)


def test_sort_x_false_preserves_order():
    """If sort_x is False, line should preserve input order."""
    fig, ax = plt.subplots()

    x = np.array([3, 1, 2])
    y_line = np.array([6, 2, 4])

    ridge_scatter_line(ax, x, y_line, sort_x=False)

    line = ax.lines[0]
    np.testing.assert_allclose(line.get_xdata(), x)
    np.testing.assert_allclose(line.get_ydata(), y_line)

    plt.close(fig)


def test_invalid_ax_raises_typeerror():
    """ax must look like a Matplotlib Axes with .plot method."""
    with pytest.raises(TypeError, match="ax must be"):
        ridge_scatter_line(None, [1, 2, 3], [1, 2, 3])


def test_mismatched_lengths_raises_valueerror():
    """x and y_line must have the same length."""
    fig, ax = plt.subplots()

    with pytest.raises(ValueError, match="same length"):
        ridge_scatter_line(ax, [1, 2, 3], [10, 20])

    plt.close(fig)


def test_non_numeric_inputs_raise_typeerror():
    """Non-numeric x/y_line should raise a clear TypeError."""
    fig, ax = plt.subplots()

    with pytest.raises(TypeError, match="numeric"):
        ridge_scatter_line(ax, ["a", "b"], [1, 2])

    with pytest.raises(TypeError, match="numeric"):
        ridge_scatter_line(ax, [1, 2], ["c", "d"])

    plt.close(fig)


def test_bad_line_kwargs_typeerror():
    """line_kwargs must be a dict or None."""
    fig, ax = plt.subplots()

    with pytest.raises(TypeError, match="line_kwargs"):
        ridge_scatter_line(ax, [1, 2], [3, 4], line_kwargs=[("lw", 2)])

    plt.close(fig)
