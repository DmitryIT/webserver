from setuptools import setup, find_packages

setup(
    name='webserver',
    version='1.0.0',
    packages=find_packages(),
    scripts = ['webserver.py', 'response.py'],
    url='www.example.com',
    license='',
    author='dmitry',
    author_email='dmitry',
    description='basic webserver'
)
