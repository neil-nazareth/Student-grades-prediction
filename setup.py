from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    """
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements=[req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

setup(
    name='mlproject',
    version='0.1',  
    author='Neil',
    author_email='neil.nazareth@gmail.com',
    description='A simple machine learning project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)