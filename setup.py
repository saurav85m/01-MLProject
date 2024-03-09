from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    This function will return the lis of requirments
    '''
    library= []
    with open (file_path,'r') as file:
        library = [line.replace("\n", "") for line in file]
            
        if HYPEN_E_DOT in library:
            library.remove(HYPEN_E_DOT)

        return library



setup(
    name='01-mlproject',
    version='0.1.0',
    author='Saurav Maulick',
    author_email='saurav85m@gmail.com',
    packages=find_packages(),
    install_requirements = get_requirements('requirements.txt')
    #install_requirements =['pandas', 'numpy']
)