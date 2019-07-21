from setuptools import setup, find_packages

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

setup(
    name='logthon',
    version='1.0.0',
    author='Giuseppe "mastrobirraio" Matranga',
    author_email='matrangagiuseppe99@gmail.com',
    license='GPLv3',
    description='A simple logger for Python',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/mastrobirraio/logthon',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)
