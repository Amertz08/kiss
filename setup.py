from setuptools import setup

__version__ = '0.1'

NAME = 'kiss'
DESCRIPTION = 'Simple static site generator'
URL = 'https://github.com/amertz08/kiss'
AUTHOR = 'Adam Mertz'
REQUIRES_PYTHON = '>=3.6.0'

setup(
    name=NAME,
    version=__version__,
    description=DESCRIPTION,
    author=AUTHOR,
    python_requires=REQUIRES_PYTHON,
    packages=['kiss'],
    include_package_data=True,
    install_requires=[
        'click==6.7',
        'jinja2==2.10',
        'pyyaml==3.12'
    ],
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    entry_points='''
        [console_scripts]
        kiss=kiss.cli:cli
    ''',
)
