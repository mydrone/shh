from setuptools import setup

version = '0.3.0'

setup(
    name='shh',
    version=version,
    url='https://github.com/wybiral/shh/',
    author='Davy Wybiral',
    author_email='davy.wybiral@gmail.com',
    description='Making Tor hidden services easy',
    keywords = 'tor onion hidden service',
    packages=['shh'],
    platforms='any',
    install_requires=[
        'stem==1.4.0',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)