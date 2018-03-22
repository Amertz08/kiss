from setuptools import setup, find_packages

setup(
    name='kiss',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click==6.7',
        'jinja2==2.10',
        'pyyaml==3.12'
    ],
    entry_points='''
        [console_scripts]
        kiss=kiss.commands:cli
    ''',
)