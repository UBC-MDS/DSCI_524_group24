# RidgeMake

RidgeMake is a lightweight, user-friendly regression and visualization package designed to take you from raw paired data to an interpretable linear fit in a few steps. It supports fitting a line of best fit by computing the slope and intercept, generating a clear scatter plot of observed points, and overlaying the fitted regression line on the same figure for immediate visual comparison. To help you assess how well the model explains the variation in your data, RidgeMake also provides an R² score calculation as a simple, standard performance metric. Together, these functions make RidgeMake a practical tool for quick exploratory analysis, teaching demonstrations, and reproducible reporting of basic linear regression results.

## Features

- `get_reg_line`: Calculate slope and intercept of the regression line
- `ridge_scatter`: Visualize your data points
- `ridge_scatter_line`: Plot the fitted line on the chart
- `ridge_get_r2`: Evaluate model performance with R² metric

## Quick example

```python
import numpy as np
from ridgemake import (
    get_reg_line,
    ridge_scatter,
    ridge_scatter_line,
    ridge_get_r2
)

# Example paired data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 6])

# Fit regression line
slope, intercept = get_reg_line(x, y)

# Compute R^2
r2 = ridge_get_r2(x, y, slope, intercept)
print(f"Slope: {slope:.3f}, Intercept: {intercept:.3f}, R^2: {r2:.3f}")

# Visualize
ridge_scatter(x, y)
ridge_scatter_line(x, y, slope, intercept)
```

## Performance expectations and limitations

RidgeMake is intended for educational use and small-to-medium sized datasets.

The package is designed for simple linear regression on paired numeric data and prioritizes clarity and ease of use over computational efficiency. It is suitable for classroom demonstrations, quick exploratory analysis, and small experiments.

RidgeMake does not support large-scale datasets, high-dimensional data, or advanced regression techniques (e.g., regularization, multivariate regression, or model diagnostics). For production-level workflows or large datasets, users should consider more specialized libraries such as scikit-learn or statsmodels.

## Developer setup

### (1) Clone the repository

```bash
git clone https://github.com/UBC-MDS/DSCI_524_group24.git
cd DSCI_524_group24
```

### (2) Set up the development environment

```bash
conda env create -f environment.yml
conda activate group-24-524
```

### (3) Install the package

From the repo root:

```bash
pip install -e .
```

## Running tests

From the repo root:

```bash
pytest -q
```

## Building documentation locally

### Generate docs locally

From the repo root, run:

```bash
quartodoc build
```

```bash
quarto render
```

## Deploying documentation

Documentation deployment is automated via GitHub Actions on pushes to `main`.

### (1) Ensure GitHub Pages is configured

On GitHub:

- Repository Settings → Pages
- Set Source to GitHub Actions

### (2) Trigger a deploy

Push to `main`:

```bash
git push origin main
```

### (3) View the deployed site

After the workflow finishes, the site will be available at the repository’s GitHub Pages URL.

## Contributors

- Yue Xiang Ni
- Suryash Chakravarty
- Seungmyun Park
- Jingyi Zha
