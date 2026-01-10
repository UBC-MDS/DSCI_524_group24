# Contributing

Contributions of all kinds are welcome here, and they are greatly appreciated! Every little bit helps, and credit will always be given.

## Contributions

You can contribute in many ways:

### Report Bugs

Report bugs by [filing an issue](https://github.com/UBC-MDS/DSCI_524_group24/issues).

**If you are reporting a bug, please follow the template guidelines. The more detailed your report, the easier and thus faster we can help you.**

### Fix Bugs

Look through the GitHub issues for bugs. Anything labelled with `bug` and `help wanted` is open to whoever wants to implement it. Please assign yourself to the issue and add a comment stating you are working on it.

### Implement Features

Look through the GitHub issues for features. Anything labelled with `enhancement` and `help wanted` is open to whoever wants to implement it. Please assign yourself to the issue and add a comment stating you are working on it.

### Write Documentation

`ridge_remake` could always use more documentation, whether as part of the official documentation, in docstrings, or even on the web in blog posts. Just [open an issue](https://github.com/UBC-MDS/DSCI_524_group24/issues) to let us know what you will be working on so that we can provide guidance.

### Submit Feedback

The best way to send feedback is to [file an issue](https://github.com/UBC-MDS/DSCI_524_group24/issues).

## Get Started!

Ready to contribute? Here's how to set up ridge_remake for
local development.

1. Fork the https://github.com/UBC-MDS/DSCI_524_group24 repository on GitHub.
2. Clone your fork locally (*if you want to work locally*)

    ```shell
    git clone git@github.com:your_name_here/ridge_remake.git
    ```

3. [Install hatch](https://hatch.pypa.io/latest/install/).

4. Create a Branch Create a branch for local development using main as a starting point.

    ```shell
    git checkout main
    git checkout -b fix-name-of-your-bugfix
    ```

    Now you can make your changes locally.

5. Test Your Changes When you're done making changes, use hatch to run the test suite and quality assurance tools.

    ```shell
    hatch run test:run
    ```

6. Commit your changes and push your branch to GitHub. Please use [semantic commit messages](https://www.conventionalcommits.org/).

    ```shell
    git add .
    git commit -m "fix: summarize your changes"
    git push -u origin fix-name-of-your-bugfix
    ```

7. Open the link displayed in the message when pushing your new branch in order to submit a pull request.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring.
3. Your pull request will automatically be checked by the full test suite.
   It needs to pass all of them before it can be considered for merging.

## Code of conduct

By contributing to this project, you are agreeing to abide by our Code of Conduct, which can be found here [Code of Conduct](https://github.com/UBC-MDS/DSCI_524_group24/blob/main/CODE_OF_CONDUCT.md).
