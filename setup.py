from setuptools import find_packages,setup
from typing import List

HYPHAN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPHAN_E_DOT in requirements:
            requirements.remove(HYPHAN_E_DOT)

        return requirements




setup(
    name='TwitterSentimentalAnalysis',
    version='0.0.1',
    author='Rakesh Kawle',
    author_email='kawlerakesh9@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)