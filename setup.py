from distutils.core import setup
from setuptools import find_packages

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
