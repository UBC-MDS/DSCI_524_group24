"""
PROMPT FOR CHATGPT:
Write pytest unit tests for ridge_scatter.

Create ONE test function: test_ridge_scatter (with 5 sub-cases).
Use matplotlib headless backend (Agg). Use explicit asserts + pytest.raises.

Cover: (1) normal case returns (ax, PathCollection) and correct point count/label,
(2) x/y length mismatch -> ValueError,
(3) empty inputs -> ValueError,
(4) non-numeric inputs -> TypeError,
(5) scatter_kwargs not dict/None -> TypeError.
Use explicit asserts + pytest.raises.
"""

import matplotlib

matplotlib.use("Agg") 
import matplotlib.pyplot as plt
import numpy as np
import pytest
from matplotlib.collections import PathCollection

from ridge_remake.ridge_scatter import ridge_scatter


def test_ridge_scatter():
    """Test ridge_scatter() creates a scatter plot and validates inputs."""
    fig, ax = plt.subplots()

    ax_out, points = ridge_scatter(
        ax,
        [1, 2, 3],
        [2, 4, 6],
        scatter_kwargs={"s": 20},
        label="data",
    )
    assert ax_out is ax
    assert isinstance(points, PathCollection)
    assert points.get_offsets().shape[0] == 3
    assert points.get_label() == "data"

    with pytest.raises(ValueError, match="same length"):
        ridge_scatter(ax, [1, 2], [1], scatter_kwargs=None)

    with pytest.raises(ValueError, match="non-empty"):
        ridge_scatter(ax, [], [], scatter_kwargs=None)

    with pytest.raises(TypeError, match="numeric"):
        ridge_scatter(ax, ["a", "b"], ["c", "d"], scatter_kwargs=None)

    with pytest.raises(TypeError, match="scatter_kwargs must be a dict"):
        ridge_scatter(ax, [1], [1], scatter_kwargs="not-a-dict")

    with pytest.raises(TypeError, match="ax"):
        ridge_scatter(None, [1, 2], [3, 4], scatter_kwargs=None)

def test_ridge_scatter_input_types():
    """
    Verify that the function handles various array-like inputs (lists, numpy arrays)
    and flattens them correctly using .ravel().
    """
    fig, ax = plt.subplots()
    
    # Nested lists or 2D arrays should be flattened without error
    x_input = [[1], [2], [3]]
    y_input = np.array([[10], [20], [30]])
    
    _, points = ridge_scatter(ax, x_input, y_input)
    
    # Resulting offsets should have shape (3, 2) representing (x, y) coordinates
    assert points.get_offsets().shape == (3, 2)
    
    plt.close(fig)

def test_ridge_scatter_visual_properties():
    """
    Verify that styling arguments in scatter_kwargs are correctly applied
    to the resulting PathCollection.
    """
    fig, ax = plt.subplots()
    
    # Test specific visual styling: size (s) and transparency (alpha)
    style = {"s": 50, "alpha": 0.5, "edgecolors": "red"}
    _, points = ridge_scatter(ax, [1], [1], scatter_kwargs=style)
    
    # PathCollection stores sizes as an array of squares of the diameters
    assert points.get_sizes()[0] == 50
    assert points.get_alpha() == 0.5
    
    plt.close(fig)