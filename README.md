# rnn_playground

TODO: Describe the purpose of this project's code.


# Setup

This section details how to get up and running with the project's code.

### Checkout

TODO: If this project makes use of `git-lfs`, then include the following. Otherwise, remove:

First, ensure that you have [`git-lfs`](https://git-lfs.github.com/) installed and connfigured on your machine.
This project's code depends on having access to local `git-lfs`'d data.

TODO: If this project uses `git` submodules, then include the following. Otherwise, remove the following:

This project makes use of [`git` submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules). As a result, on your
first `git clone`, it is crucial to make sure that you obtain the _code_ from these submodules! If this is your first
clone, then use the `--recursive` flag as.

If you have already executed `git clone` without the `--recursive` flag, then perform the following commands from the
root of this repository:
```bash
git submodule init
git submodule update
```

TODO: If none of the above apply, then remove this entire sub-section!

### Environment

To get ready for development, execute the following from within the project's root:
```
conda env create
source activate rnn_playground
```

Then, to package the code, build any cython, C, or C++ code, download the `spacy` english model, and typecheck the
project, execute:
```bash
python setup.py build
```

### Development

To make this code available for import from other projects in your virtual environment (which is managed by `conda`),
use the `develop` setuptools command:
```bash
python setup.py develop
```

This `develop` command is necessary for both running tests and interacting with the code as you work within the project.

After, you may execute tests by invoking the `pytest` command from the repoistory root. For example, the following is a
common invocation:
```bash
pytest -s 
```

NOTE: If you **do** have Cython, C, or C++ files, you **must** re-run `python setup.py build` on each change
_before_ running tests. This is because the Cython, C, or C++ files must be recompiled. If you change Python code only,
you do not need to re-run `build`.

### Type checking

To run static type checking on all of the project's python files, which are located under `src/` and `tests/`, execute
the following `mypy` command:
```bash
mypy --ignore-missing-imports `find src/ tests/ -type f -name "*.py"`
```

A zero exit code means that all code type checks. A non-zero exit code will have accompanying type errors printed to
stdout.

NOTE: The `--ignore-missing-imports` flag is only useful here because we don't have the proper _stub_ files for many of
our 3rd party projects. If available, use the appropriate stub files.

### Documentation and Code Coverage

To see the line-by-line code coverage of your tests, use `coverage` from the root of this project:
```bash
coverage run --source src -m py.test && coverage report && coverage html
```

To build documentation, use `sphinx`:
```bash
cd docs && make html
```

# Project Architecture and Functionality

TODO: Explain and describe the important pieces of code, their functionality, how they interact (or do not) with one
another, and how they all relate to the project's purpose.

