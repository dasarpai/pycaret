"""Utility methods to print system info for debugging.
adapted from :func:`sktime.show_versions`
adapted from :func:`sklearn.show_versions`
"""

__author__ = ["Nikhil Gupta"]
__all__ = ["show_versions"]

import importlib
import platform
import sys


required_deps = [
    "pip",
    "setuptools",
    "pycaret",
    "ipython",
    "ipywidgets",
    "numpy",
    "pandas",
    "jinja2",
    "scipy",
    "joblib",
    "sklearn",
    "pyod",
    "imblearn",
    "category_encoders",
    "lightgbm",
    "numba",
    "requests",
    "matplotlib",
    "scikitplot",
    "yellowbrick",
    "plotly",
    "kaleido",
    "statsmodels",
    "sktime",
    "tbats",
    "pmdarima",
]

optional_deps = [
    "shap",
    "interpret",
    "umap",
    "pandas_profiling",
    "explainerdashboard",
    "autoviz",
    "fairlearn",
    "xgboost",
    "catboost",
    "kmodes",
    "mlxtend",
    "tune_sklearn",
    "ray",
    "hyperopt",
    "optuna",
    "skopt",
    "mlflow",
    "gradio",
    "fastapi",
    "uvicorn",
    "m2cgen",
    "evidently",
    "nltk",
    "pyLDAvis",
    "gensim",
    "spacy",
    "wordcloud",
    "textblob",
    "psutil",
    "fugue",
    "streamlit",
    "prophet",
]


def _get_sys_info():
    """
    System information.
    Return
    ------
    sys_info : dict
        system and Python version information
    """
    python = sys.version.replace("\n", " ")

    blob = [
        ("python", python),
        ("executable", sys.executable),
        ("machine", platform.platform()),
    ]

    return dict(blob)


def _get_deps_info(optional: bool = False):
    """
    Overview of the installed version of dependencies.

    Parameters
    ----------
    optional : bool, optional
        If False returns the required library versions, if True, returns
        optional library versions, by default False.

    Returns
    -------
    deps_info: dict
        version information on relevant Python libraries
    """

    def get_version(module):
        return module.__version__

    deps_info = {}

    if optional:
        deps = optional_deps
    else:
        deps = required_deps

    for modname in deps:
        try:
            if modname in sys.modules:
                mod = sys.modules[modname]
            else:
                mod = importlib.import_module(modname)
            ver = get_version(mod)
            deps_info[modname] = ver
        except ImportError:
            deps_info[modname] = "Not installed"
        except AttributeError:
            #### Version could not be obtained
            deps_info[modname] = "Installed but version unavailable"

    return deps_info


def show_versions(optional: bool = True):
    """Print useful debugging information (e.g. versions).

    Parameters
    ----------
    optional : bool, optional
        Should optional dependencies be documented, by default True
    """
    print("\nSystem:")  # noqa: T001
    sys_info = _get_sys_info()
    for k, stat in sys_info.items():
        print("{k:>10}: {stat}".format(k=k, stat=stat))  # noqa: T001

    print("\nPython required dependencies:")  # noqa: T001
    optional_deps_info = _get_deps_info()
    for k, stat in optional_deps_info.items():
        print("{k:>20}: {stat}".format(k=k, stat=stat))  # noqa: T001

    if optional:
        print("\nPython optional dependencies:")  # noqa: T001
        optional_deps_info = _get_deps_info(optional=True)
        for k, stat in optional_deps_info.items():
            print("{k:>20}: {stat}".format(k=k, stat=stat))  # noqa: T001