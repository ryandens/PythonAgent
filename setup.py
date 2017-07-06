from setuptools import setup

setup(
    name='python-agent',
    description='Python Agent',
    version="0.0.0.1",
    test_suite="python_agent.tests",
    url='',
    author='Ryan Dens',
    author_email='ryan.dens@jhu.edu',
    license='MIT',
    packages=['python_agent'],
    install_requires=[
          'guppy',
    ]
)