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

def test_ridge_scatter_single_point():
    """
    Edge Case 1: Minimal Input
    Verify the function can handle a single data point without crashing.
    """
    fig, ax = plt.subplots()
    x, y = [1.0], [2.0]
    
    returned_ax, points = ridge_scatter(ax, x, y)
    
    assert returned_ax is ax
    assert len(points.get_offsets()) == 1
    plt.close(fig)

def test_ridge_scatter_custom_kwargs():
    """
    Edge Case 2: Custom Styling
    Verify that scatter_kwargs are correctly passed to the matplotlib artist.
    """
    fig, ax = plt.subplots()
    x, y = [1, 2, 3], [4, 5, 6]
    kwargs = {"alpha": 0.5, "s": 100}
    
    _, points = ridge_scatter(ax, x, y, scatter_kwargs=kwargs)
    
    assert points.get_alpha() == 0.5
    assert points.get_sizes()[0] == 100
    plt.close(fig)

def test_ridge_scatter_with_label():
    """
    Edge Case 3: Legend Labeling
    Verify that the label is correctly applied to the PathCollection for legends.
    """
    fig, ax = plt.subplots()
    x, y = [1, 2], [3, 4]
    label_text = "Training Data"
    
    _, points = ridge_scatter(ax, x, y, label=label_text)
    
    assert points.get_label() == label_text
    plt.close(fig)

# --- Error Cases (Defensive Programming) ---
def test_ridge_scatter_invalid_axes():
    """
    Error Case 1: Invalid Axes Object
    Confirm TypeError is raised if ax is None or not a matplotlib Axes object.
    """
    with pytest.raises(TypeError, match="must be a Matplotlib Axes-like object"):
        ridge_scatter(None, [1, 2], [3, 4])

def test_ridge_scatter_shape_mismatch():
    """
    Error Case 2: Array Length Mismatch
    Confirm ValueError is raised when x and y have different lengths.
    """
    fig, ax = plt.subplots()
    x = [1, 2, 3]
    y = [1, 2]  # Shorter than x
    
    with pytest.raises(ValueError, match="same length"):
        ridge_scatter(ax, x, y)
    plt.close(fig)

def test_ridge_scatter_empty_input():
    """
    Error Case 3: Empty Inputs
    Confirm ValueError is raised when empty arrays are provided.
    """
    fig, ax = plt.subplots()
    with pytest.raises(ValueError, match="non-empty"):
        ridge_scatter(ax, [], [])
    plt.close(fig)
