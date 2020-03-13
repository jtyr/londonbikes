#!/usr/bin/env python

from distutils.core import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name='londonbikes',
    version='1.0.0',
    description='Script which allows to search in the TFL BikePoint API.',
    author='Jiri Tyr',
    author_email='jiri.tyr@gmail.com',
    url='http://github.com/jtyr/londonbikes',
    license='MIT',
    keywords='london bike bikepoint tfl api',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Markup :: XML'
    ],
    long_description=long_description,
    scripts=['londonbikes'],
    install_requires=['docopt', 'requests'],
    data_files=[
        ('share/doc/londonbikes', ['LICENSE', 'README.md'])
    ]
)
