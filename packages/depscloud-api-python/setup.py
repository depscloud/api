from setuptools import setup, find_packages

setup(
    name='depscloud_api',
    version='0.1.18',
    license='MIT',
    description='Python client to the deps.cloud API',
    author='deps.cloud Authors',
    url='https://deps.cloud/',
    install_requires=[
        "protobuf==3.13.0",
        "grpcio==1.33.1"
    ],
    packages=find_packages()
)
