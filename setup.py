from setuptools import setup
from setuptools import find_packages

from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
    requirements = [x.strip() for x in content]

setup(
    name='taxi_package',  # To find the package name within the folder
    description="functions for taxi project",  # Whatever you want
    packages=find_packages(),
    install_requires=requirements,  # To list the necessary libraries
    scripts=['scripts/me-2-manhattan'
             ])  # If you want to install any python script
