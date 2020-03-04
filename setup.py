from setuptools import setup

setup(
    name='webserver',
    version='1.0.4',
    packages=['webserver'],
    entry_points={
        "console_scripts":[
            "my_webserver = webserver.webserver_runner:run",
            "get_response = webserver.response:get_response"
        ]
    },
    url='www.example.com',
    license='',
    author='dmitry',
    author_email='dmitry',
    description='basic webserver'
)
