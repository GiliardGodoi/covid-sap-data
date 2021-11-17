import re
from setuptools import setup, find_packages

setup(
    name='covidsap',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'openpyxl',
        'seaborn', 'matplotlib', 'pandas',
        'rich', 'click'
    ],
    entry_points={
        'console_scripts': [
            'covidsap = src.main:cli',
        ],
    },
)