from setuptools import setup, find_packages

setup(
    name="debugegg",
    version="1.0.0",
    packages=find_packages(),
    description="A simple python package for debugging.",
    author="Egglord",
    python_requires=">=3.7",
    install_requires=[
        "colorama>=0.4.7",
    ]
)
