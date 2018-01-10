#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from glob import glob
import os
from os.path import basename, splitext
from sys import exit

from setuptools import find_packages
from setuptools.command.build_py import build_py
try:
    from numpy.distutils.core import setup
except:
    from setuptools import setup


# Inspired from the following setup.py's:
#
# https://github.com/scikit-learn/scikit-learn/blob/master/setup.py
# https://github.com/numpy/numpy/blob/master/setup.py
# https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure

def do_typecheck() -> None:
    print("Typechecking...", end='')
    from mypy import api
    typing_result = api.run(['--ignore-missing-imports', 'src/'] +
                            list(py_files_only('tests')))
    stdout, stderr, exit_status = typing_result[0], typing_result[1], int(typing_result[2])
    if exit_status != 0:
        print("\nType check failed. Error message:")
        print("----")
        print(stdout)
        print("")
        print("ERROR: Project failed to typecheck.")
        exit(1)
    print("checks out.")

def py_files_only(start):
    for root, rest, files in os.walk(start):
        if len(rest) == 0:
            name = lambda f: "%s/%s" % (root, f)
            for f in files:
                if f.endswith('.py'):
                    yield name(f)

def download_spacy_model(model_name: str = 'en_core_web_md') -> None:
    import spacy
    model_path = spacy.util.get_data_path() / spacy.deprecated.resolve_model_name(model_name)
    if not model_path.exists():
        try:
            print("Downloading spacy language model: %s" % model_name)
            spacy.cli.download(model_name)
        except SystemExit as e:
            if e.code != 0:
                raise

class BuildCmd(build_py):
    """Customized python build step."""

    def run(self):
        # Performs static type checking.
        do_typecheck()

        

        # Does the "normal" build process.
        build_py.run(self)

setup(
    name='rnn_playground',

    # Use semantic versioning 2.0: http://semver.org/
    version='0.0.0',

    # Use our custom build command
    cmdclass={'build_py': BuildCmd},

    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],


    # `pytest` integration
    # http://doc.pytest.org/en/latest/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner
    setup_requires=[
        #
        # Add more here !!!
        #
        'Cython',
        'pytest-runner',
        'pytest-raisesregexp',
    ],
    tests_require=[
        #
        # Add any dependencies that are _only_ required for tests here!
        #
        'pytest',
    ],

    # The package cannot run out of an .egg file.
    # https://setuptools.readthedocs.io/en/latest/setuptools.html#id8
    zip_safe=False,
    include_package_data=True,

    # Executable scripts w/in this project.
    scripts=[
        # put the names of all executable scripts here!
        # see:
        # https://stackoverflow.com/questions/16742203/create-a-python-executable-using-setuptools/16745122#16745122
    ],
    entry_points={
        'console_scripts': [
            'rnn_playground=rnn_play.rnn_playground:main',
        ]
    },
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
)
