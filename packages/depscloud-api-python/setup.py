from setuptools import setup, find_packages

setup(
    name='depscloud_api',
    version='0.1.19',
    license='MIT',
    description='Python client to the deps.cloud API',
    author='deps.cloud Authors',
    url='https://deps.cloud/',
    install_requires=[
        "protobuf==3.14.0",
        "grpcio==1.33.2"
    ],
    packages=find_packages()
)
