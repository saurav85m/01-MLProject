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
    
if __name__== "__main__":
   aaa = get_requirements("requirements.txt")
   print(aaa)