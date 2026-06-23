from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Returns a list of requirements"""
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt") as file:
            # read lines from file
            lines=file.readlines()
            #process eeach line
            for line in lines:
                requirement=line.strip()
                ##ignore empty lines and -e
                if requirement and requirement!="-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_lst   
setup(
    name="network-security",
    version="0.0.1",
    author="Maddi  Balaji",
    packages=find_packages(),
    install_requires=get_requirements()     
)
    