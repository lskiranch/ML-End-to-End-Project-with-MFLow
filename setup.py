from setuptools import setup, find_packages

setup(
    name="ml-flow",
    version="0.1.0",
    description="Add your description here",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.12",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "mlflow",
        "notebook",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "python-box",
        "pyYAML",
        "tqdm",
        "ensure",
        "joblib",
        "types-PyYAML",
        "Flask",
        "Flask-Cors"
    ],
)
