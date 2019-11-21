from setuptools import setup


setup(
	name = 'joke-cli',
	version = '0.1.0',
	packages = 'joke-cli',
	entry_points = {
		'console_scripts': [ 'joke-cli = joke-cli.__main__:main' ]
	})