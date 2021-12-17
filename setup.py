import setuptools
from setuptools import setup
from setuptools import find_packages

# with open('README.md') as f:
#     long_description = f.read()

setuptools.setup(
    name="Shell_FE_Appium_Core",
    version='1.0.0a8',
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
