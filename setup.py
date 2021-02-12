from setuptools import setup

setup(
   name='tspam',
   version='0.1',
   description='A very simple sms-spammer',
   author='AndreyBorisov',
   author_email='andrey.borisov@outlook.de',
   packages=['tspam'],  #same as name
   entry_points={'console_scripts': [ 'tspam=tspam.start:MAIN']},
       # function to call on $ python my.egg
    py_modules=['tspam=tspam.start:MAIN'],
    license="MPL 2.0",
   install_requires=['asyncio', 'aiohttp', "requests", "colorama"], #external packages as dependencies
)
