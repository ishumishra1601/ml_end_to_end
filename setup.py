from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    rewuirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]


setup(
    name = 'ML End to End Project',
    version = '0.0.1',
    author = "Ishu mishra",
    autor_email = 'ishumishra500@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)