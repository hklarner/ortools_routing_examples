

from setuptools import find_packages
from setuptools import setup


setup(
    name="routing",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click==7.1.2",
        "pydantic==1.7.3",
        "ortools==7.6.7691",
        "pandas==1.1.0",
        "matplotlib"
    ],
    entry_points="""
        [console_scripts]
        routing=main:main
    """
)


