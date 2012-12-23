from setuptools import setup, find_packages

setup(
    name='blimp',
    version='0.0.1',
    author='Jose Padilla',
    author_email='jpadilla@getblimp.com',
    packages=find_packages(),
    url='https://github.com/getblimp/blimp-python/',
    license='MIT License',
    description='Blimp library for Python',
    long_description='Blimp library for Python',
    install_requires=[
        'requests'
    ],
)
