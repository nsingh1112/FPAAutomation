import setuptools
from setuptools import setup
from setuptools import find_packages

# with open('README.md') as f:
#     long_description = f.read()

setuptools.setup(
    name="Shell-FE-Appium-Core",
    version='2.0.0b1',
    author="Sakthivel Rajasekar",
    author_email="saktivel.rajasekar@shell.com",
    description="Appium Core package to be used along with the Shell FE Behave framework for Mobile automation.",
    # long_description=long_description,
    long_description_content_type='text/markdown',
    license="Proprietary",
    classifiers=[
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent'
    ],
    packages=setuptools.find_packages(exclude=["Shell_FE_Behave_Tests"]),
    # install_requires=[
    #     'selenium',
    #     'webdriver-manager',
    #     'msedge-selenium-tools',
    #     'openpyxl'
    # ],
    python_requires='>=3.9'

)
