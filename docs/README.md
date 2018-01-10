# Documentation

To build documentation run (from this directory):

    make html

and the generated documentation will be under `_build/html`.

## Style

The (at least initial) style follows the
[NumPy Docstring Standard](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt#docstring-standard),
with the single modification of placing empty lines between parameters and return values
(see [`scikit-learn`](http://scikit-learn.org/stable/)).


## Details

The initial [conf.py](conf.py) and [Makefile](Makefile) were generated
using
[`sphinx-quickstart`](http://www.sphinx-doc.org/en/stable/invocation.html#invocation-of-sphinx-quickstart) and
then updated accordingly.
[`sphinx-apidoc`](http://www.sphinx-doc.org/en/stable/invocation.html#invocation-apidoc) is used to
automatically generate the
[reStructuredText](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html) files for
the [rnn_play](../rnn_play) package, which in turn utilizes the
[`sphinx.ext.autodoc`](http://www.sphinx-doc.org/en/stable/ext/autodoc.html#module-sphinx.ext.autodoc) extension
to parse the Python docstrings.
