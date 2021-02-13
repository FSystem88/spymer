from setuptools import setup

setup(
   name='tspymer',
   version='0.1',
   description='A very simple sms-spammer',
   packages=['tspymer'],  #same as name
   package_dir={'tspymer': 'src/tspymer_mobile'},
   package_data={'tspymer': ['data/*.json']},
   include_package_data=True,
   entry_points={'console_scripts': [ 'tspymer=tspymer.start:MAIN']},
   # function to call on $ python my.egg
   py_modules=['tspymer.start:MAIN'],
   license="MPL 2.0",
   install_requires=[ "requests", "colorama","urllib3"], #external packages as dependencies
)
