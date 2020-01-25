from setuptools import setup


setup(
    name='log-parser',
    version='0.1.0',
    packages=['log_parser'],
    entry_points={
        'console_scripts': [
            'log-parser = log_parser.__main__:runner'
        ]
    }
)
