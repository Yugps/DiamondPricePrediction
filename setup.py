from setuptools import find_packages,setup
from typing import List

hyphen_e_dot='-e .' # this -e . in requirements.txt basically triggers setup.py file wihtout needing to run it hence creates the package automatically

def get_requirements_file(file_path): # what we have done here is we have replaced /n i.e line change with '' space then we have returned the data
    requirements=[]                   # from the requiremnts.txt file 
    with open(file_path,'r') as f:
        requirements=f.readlines()
        final_requirements=[req.replace('/n','') for req in requirements]
        if hyphen_e_dot in final_requirements: # to delete the -e . in requirements.txt as we don't want to install that library
            final_requirements.remove(hyphen_e_dot)
        return final_requirements



setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='YugPratapSingh',
    author_email='yugpratapsingh8@gmail.com',
    install_requires=get_requirements_file('requirements.txt'), # this will automatically get the packages from requiremnts.txt due to above created function
    packages=find_packages() # this will find all the module and packages within our project structure 
    )