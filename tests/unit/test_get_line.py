"""
A test module that tests the get_reg_line module.

This file contains tests which are used to test the output of the function
get_reg_line(), in the get_reg_line module. The tests can be run by calling 
pytest -v . in the root directory

Prompt used to generate test cases-->

Create Test-Driven Development tests for the function get_reg_line. Please 
generate some edge cases where the function might provide incorrect reponses
or fail. As well, please add appropriate failure messages so that the user
can quickly tell why the function failed.

LLM used: Google Gemini
"""
import numpy as np
import pandas as pd
import pytest

from ridge_remake.get_reg_line import get_reg_line

def test_perfect_linear_relationship():
    """Verify that y_pred matches y exactly in a noise-free linear system."""
    X = np.array([[1], [2], [3], [4]])
    y = np.array([2, 4, 6, 8]) # y = 2x + 0
    y_pred = get_reg_line(X, y)
    np.testing.assert_allclose(y_pred, y, rtol=1e-5)

def test_intercept_only():
    """Verify the model handles a flat line (slope = 0)."""
    X = np.array([[1], [2], [3]])
    y = np.array([5, 5, 5])
    y_pred = get_reg_line(X, y)
    np.testing.assert_allclose(y_pred, [5, 5, 5])

def test_multicollinearity_failure():
    """
    Verify that np.linalg.inv raises LinAlgError when features are 
    perfectly collinear (Singular Matrix).
    """
    # Column 2 is exactly 2x Column 1
    X = np.array([[1, 2], 
                  [2, 4], 
                  [3, 6]])
    y = np.array([1, 2, 3])
    with pytest.raises(np.linalg.LinAlgError):
        get_reg_line(X, y)

def test_high_dimensional_input():
    """Ensure shape consistency with multiple features."""
    X = np.random.rand(10, 5)
    y = np.random.rand(10)
    y_pred = get_reg_line(X, y)
    assert y_pred.shape == (10,)

def test_pandas_compatibility():
    """Ensure the function handles DataFrame/Series inputs via np.asarray."""
    X = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 7]}) 
    y = pd.Series([10, 20, 30])
    y_pred = get_reg_line(X, y)
    assert isinstance(y_pred, np.ndarray)
    assert len(y_pred) == 3

def test_mismatched_dimensions():
    """
    Verify that providing X and y with a different number of samples 
    raises a ValueError during matrix multiplication.
    """
    # X has 3 samples, but y only has 2 samples
    X = np.array([[1], [2], [3]])
    y = np.array([1, 2])
    
    # NumPy's matrix multiplication (@) will raise ValueError due to dimension mismatch
    with pytest.raises(ValueError):
        get_reg_line(X, y)

def test_multi_target_regression():
    """
    Verify that the function can handle multiple targets (y) simultaneously.
    If y is (n_samples, n_targets), y_pred should also be (n_samples, n_targets).
    """
    X = np.array([[1], [2], [3]])
    # Target 1: y = 2x, Target 2: y = 10x
    y = np.array([[2, 10], 
                  [4, 20], 
                  [6, 30]])
    
    y_pred = get_reg_line(X, y)
    
    # Check if the output shape matches the multi-target input shape
    assert y_pred.shape == (3, 2)
    # Check if the predictions are accurate for both targets
    np.testing.assert_allclose(y_pred, y, rtol=1e-5)