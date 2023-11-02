from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='This repo can be used to generate primers from fasta or genbank files automatically. It can also remove the signal peptides by incorporating functions to read SignalP outputs.',
    author='Technical University of Denmark (DTU)',
    license='MIT',
)
