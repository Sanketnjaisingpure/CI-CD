from setuptools import find_packages ,setup 
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirement(file_path:str )->List[str]:
    """ 
    This Functions will returns  the list of requirements
    """
    requirement = []
    with open(file_path) as file_obj:

        requirement  = file_obj.readlines()
        # This above functions read the file requrirements in line by line ,and hence it also read next line '\n' 
        # hence we replace that new line '\n' with "" 
        # if we are adding new packages , then we write -e . it automatically triggers the packages and 
        # appends in the requriement.txt file   
        requirement = [ req.replace("\n" ,"") for req in requirement ] 

        if HYPEN_E_DOT in requirement :
            requirement.remove(HYPEN_E_DOT)
        return requirement

setup(
        name = 'mlproject Ci-Cd' ,
        version= '0.0.1' ,
        author = 'Sanket',
        author_email='sanketnjaisingpure14@gmail.com',
        packages=find_packages() , 
        install_requires = get_requirement('requirement.txt')

)