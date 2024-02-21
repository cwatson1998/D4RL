from distutils.core import setup
from setuptools import find_packages

# The mjrl probably has to be hand-picked, look at the git history of this repo to see my favorite choice.
setup(
    name='d4rl',
    version='1.0',
    install_requires=['gym', 
                      'numpy', 
                      'mujoco_py', 
                      'h5py', 
                      'mjrl'],
    packages=find_packages(),
)
