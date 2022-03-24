import setuptools

setuptools.setup(
    name="Shell_FE_Requests_Core",
    version='1.0.0a1',
    author="Functional Excellence Team",
    author_email="praveen.kumara@shell.com",
    description="Requests Core package to be used along with the Shell FE Behave framework for API automation.",
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
