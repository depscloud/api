from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='depscloud_api',
    version='0.1.5',
    description='Python client to the deps.cloud API',
    long_description=readme,
    author='deps.cloud Authors',
    url='https://deps.cloud/',
    license=license,
    packages=find_packages()
)
