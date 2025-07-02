from setuptools import setup, find_packages

setup(
    name="src",
    version="0.1.0",
    description="Residual analysis tools for Eddy3D CFD simulations",
    author="Your Name",
    author_email="your@email.com",
    packages=find_packages(),
    install_requires=[
        "matplotlib>=3.4",
        "pandas>=1.3",
        "tqdm>=4.60"
    ],
    python_requires=">=3.7",
)