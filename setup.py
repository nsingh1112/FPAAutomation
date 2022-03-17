import setuptools
from setuptools import setup
from setuptools import find_packages

setuptools.setup(
    name="Shell-FE-Selenium-Core",
    version='1.0.0a2',
    author="Praveen Kumar Appusamy",
    author_email="praveen.kumara@shell.com",
    description="Selenium Core package to be used along with the Shell FE Behave framework for UI automation.",
    long_description_content_type='text/markdown',
    license="Proprietary",
    classifiers=[
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent'
    ],
    packages=setuptools.find_packages(exclude=["Shell_FE_Behave_Tests"]),
    python_requires='>=3.9'
)
