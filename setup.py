import os
import re
from setuptools import setup, find_packages


def parse_version(path):
    """Extract the `__version__` string from the given file"""
    with open(path, 'r') as fp:
        version_file = fp.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Classifiers
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    ('License :: OSI Approved :: GNU General Public License v3 or later '
        '(GPLv3+)'),
    'Operating System :: POSIX',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]


###############################################################################
# Call setup() ################################################################
###############################################################################
setup(
    name="helpme",
    version=parse_version(os.path.join('helpme', 'version.py')),
    author=("Tanner Prestegard"),
    author_email="tprestegard@gmail.com",
    description="A Python package for accessing the GraceDB API.",
    license='GPL-3.0-or-later',
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    install_requires=("Click==7.0",),
    entry_points={
        "console_scripts": ("helpme=helpme.script:main",)
    },
)
