from setuptools import setup, find_packages

__version__ = "1.0"
setup(
    name="cses-problem-set",
    version=__version__,
    python_requires="~=3.7",
    install_requires=[],
    extras_require={
        "tests": ["black~=19.10b0", "mypy>=0.780", "pytest>=5.4.2", "pytest-cov>=2.9.0"]
    },
    packages=find_packages("src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={"": "src"},
    include_package_data=True,
    description="Tested solutions to the CSES problem set in Python3",
    license="MIT",
    author="seahrh",
    author_email="seahrh@gmail.com",
    url="https://github.com/seahrh/cses-problem-set-python",
)
