import setuptools
from setuptools import setup
from setuptools import find_packages

setuptools.setup(
    name="Shell_FE_Selenium_Core",
    version='1.0.0a1',
    author="Praveen Kumar Appusamy",
    author_email="praveen.kumara@shell.com",
    description="Selenium Core package to be used along with the Shell FE Behave framework for UI automation.",
    license="Proprietary",
    classifiers=[
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent'
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        'selenium',
        'webdriver-manager',
        'msedge-selenium-tools',
        'openpyxl'
    ],
    python_requires='>=3.9'
)
