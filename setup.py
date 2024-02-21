from distutils.core import setup
from setuptools import find_packages

setup(
    name='d4rl',
    version='1.0',
    install_requires=['gym', 
                      'numpy', 
                      'mujoco_py', 
                      'h5py', 
                      'mjrl @ git+git://github.com/aravindr93/mjrl@a38324680e76347bfc5040114017b443060b1e0d'],
    packages=find_packages(),
)
