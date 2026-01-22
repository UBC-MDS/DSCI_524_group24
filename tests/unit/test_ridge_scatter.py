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
