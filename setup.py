from setuptools import setup, find_packages

setup(
    name="metaphor-api-project",
    version="0.1",
    packages=find_packages(),
    author="Vivian Le",
    install_requires=[
        "Flask==2.0.3", 
        "Jinja2==2.11.3", 
        "metaphor-python==0.1.16", 
        "requests==2.27.1"],
)