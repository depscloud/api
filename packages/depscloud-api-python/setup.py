from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='depscloud_api',
    version='0.1.5',
    description='Python client to the deps.cloud API',
    author='deps.cloud Authors',
    url='https://deps.cloud/',
    packages=find_packages()
)
