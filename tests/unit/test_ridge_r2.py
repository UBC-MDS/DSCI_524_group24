import pytest
import numpy as np
from ridge_remake.ridge_r2 import ridge_get_r2

def test_r2_constant_target():
    """
    Edge Case 1: Zero Variance in True Values
    When y_true is constant (e.g., [2, 2, 2]), SS_tot becomes 0.
    Division by zero should be handled. Standard behavior (like sklearn) 
    is to return 0.0 or a defined constant to avoid crashing.
    """
    y_true = np.array([2.0, 2.0, 2.0])
    y_pred = np.array([2.0, 2.0, 2.0])
    # Note: Depending on implementation, you might expect 1.0, 0.0, or a Warning.
    # Here we check if it handles it without crashing.
    result = ridge_get_r2(y_true, y_pred)
    assert np.isfinite(result)

def test_r2_single_sample():
    """
    Edge Case 2: Single Data Point
    With only one sample, the variance (SS_tot) cannot be calculated 
    (it is effectively 0). This tests the function's stability with minimal input.
    """
    y_true = np.array([10.0])
    y_pred = np.array([11.0])
    result = ridge_get_r2(y_true, y_pred)
    assert isinstance(result, float)

def test_r2_very_large_values():
    """
    Edge Case 3: Numerical Stability (Large Values)
    Tests if the function handles very large floats without overflowing 
    during the squaring process (Σx²).
    """
    y_true = np.array([1e10, 2e10, 3e10])
    y_pred = np.array([1.1e10, 1.9e10, 3.2e10])
    result = ridge_get_r2(y_true, y_pred)
    # R2 is a ratio, so it should still be a reasonable number between -inf and 1
    assert 0.0 < result < 1.0

def test_r2_all_zeros():
    """
    Edge Case 4: All Zero Inputs
    Tests the behavior when both true and predicted values are zero.
    This is a subset of the constant target case but common in sparse data.
    """
    y_true = np.zeros(5)
    y_pred = np.zeros(5)
    result = ridge_get_r2(y_true, y_pred)
    assert result == pytest.approx(1.0) or result == pytest.approx(0.0)

def test_r2_empty_arrays():
    """
    Edge Case 5: Empty Input
    Ensures that passing empty arrays raises an appropriate error 
    rather than returning a confusing calculation result.
    """
    y_true = np.array([])
    y_pred = np.array([])
    with pytest.raises(ValueError):
        ridge_get_r2(y_true, y_pred)