from setuptools import setup

setup(
    name='overwriteable-config',
    version='0.0.1',
    description='Simple Overwriteable Config',
    author='Casey Peat',
    author_email='caseypeat@protonmail.com',
    url='https://github.com/caseypeat/configyaml',
    packages=['config'],
    python_requires=">=3.7",
    install_requires=['pyyaml'],
)