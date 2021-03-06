# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from setuptools import setup

REQUIRES = [
    'recognizers-date-time>=1.0.0a1',
    'recognizers-number-with-unit>=1.0.0a1',
    'recognizers-number>=1.0.0a2',
    'recognizers-text>=1.0.0a1', 
    'botbuilder-schema>=4.4.0b1',
    'botframework-connector>=4.4.0b1',
    'botbuilder-core>=4.4.0b1']

TEST_REQUIRES = [
    'aiounittest>=1.1.0'
]

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, 'botbuilder', 'dialogs', 'about.py')) as f:
    package_info = {}
    info = f.read()
    exec(info, package_info)

setup(
    name=package_info['__title__'],
    version=package_info['__version__'],
    url=package_info['__uri__'],
    author=package_info['__author__'],
    description=package_info['__description__'],
    keywords=['BotBuilderDialogs', 'bots', 'ai', 'botframework', 'botbuilder'],
    long_description=package_info['__summary__'],
    license=package_info['__license__'],
    packages=['botbuilder.dialogs', 'botbuilder.dialogs.prompts', 'botbuilder.dialogs.choices'],
    install_requires=REQUIRES + TEST_REQUIRES,
    tests_require=TEST_REQUIRES,
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]
)
