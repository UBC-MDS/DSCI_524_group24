# RidgeMake

RidgeMake is a lightweight, user-friendly regression and visualization package designed to take you from raw paired data to an interpretable linear fit in a few steps. It supports fitting a line of best fit by computing the slope and intercept, generating a clear scatter plot of observed points, and overlaying the fitted regression line on the same figure for immediate visual comparison. To help you assess how well the model explains the variation in your data, RidgeMake also provides an R² score calculation as a simple, standard performance metric. Together, these functions make RidgeMake a practical tool for quick exploratory analysis, teaching demonstrations, and reproducible reporting of basic linear regression results.

## Features

-   `get_reg_line`: Calculate slope and intercept of the regression line
-   `ridge_scatter`: Visualize your data points
-   `ridge_scatter_line`: Plot the fitted line on the chart
-   `ridge_get_r2`: Evaluate model performance with R² metric

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

If you are developing locally:

```bash
pip install -e .
```

If you are installing from a released package (example):

```bash
pip install ridge_remake
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

After the workflow finishes, the site will be available at the repository’s GitHub Pages URL:
https://ubc-mds.github.io/DSCI_524_group24/


## Contributors

-   Yue Xiang Ni
-   Suryash Chakravarty
-   Seungmyun Park
-   Jingyi Zha
