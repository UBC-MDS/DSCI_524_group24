# MIT License
#
# Copyright (c) 2026 suryash chakravarty
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Add a docstring here for the init module.

This might include a very brief description of the package,
its purpose, and any important notes.
"""


"""RidgeMake: lightweight regression + plotting helpers.

This package provides:
- get_reg_line: fit a simple regression line to paired data
- ridge_scatter: scatter plot for paired data
- ridge_scatter_line: overlay the fitted line on the scatter plot
- ridge_get_r2: compute R^2 from y_true and y_pred
"""

from .get_reg_line import get_reg_line
from .ridge_scatter import ridge_scatter
from .ridge_scatter_line import ridge_scatter_line
from .ridge_r2 import ridge_get_r2

__all__ = [
    "get_reg_line",
    "ridge_scatter",
    "ridge_scatter_line",
    "ridge_get_r2",
]
