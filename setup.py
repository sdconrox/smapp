from setuptools import setup, find_packages

setup(
    name='smapp',
    version='0.1.0',
    description='A tool for generating and submitting randomized fake login data for educational and ethical cybersecurity research purposes.',
    author='Shane Conroy',
    author_email='sdconrox@gmail.com',
    url='https://sdconrox.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'faker',
    ],
    include_package_data=True,
)