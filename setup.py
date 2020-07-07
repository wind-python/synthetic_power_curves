import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="synthetic_power_curves",
    version="0.0.1dev",
    description="Creating synthetic wind turbine power curves.",
    url="http://github.com/wind-python/windpowerlib",
    author="oemof developer group",
    author_email="windpowerlib@rl-institut.de",
    license="MIT",
    packages=["synthetic_power_curves"],
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    zip_safe=False,
    install_requires=["pandas >= 0.20.0"],
    extras_require={
        "dev": [
            "pytest",
            "jupyter",
            "sphinx_rtd_theme",
            "nbformat",
            "numpy",
            "matplotlib",
        ]
    },
)
