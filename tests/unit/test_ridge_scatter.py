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
