from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    HYPHEN='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("\n", "")for req in requirements]

        if HYPHEN in requirements:
            requirements.remove(HYPHEN)
    return requirements

setup(
name= 'mlprojects',
version= '0.0.1',
author= 'Ankan',
author_email='ankanchakraborty12345@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)