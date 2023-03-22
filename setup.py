from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    """
    This function will return list of requirements

    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            # -e . enables setup.py file to build packages
            requirements.remove('-e .')
    
    return requirements


setup(
    name="MLproject",
    version="0.0.1",
    author="Shambhuraj",
    author_email="shambhurajpatil11@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)