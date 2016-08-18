import io

import setuptools
from setuptools import find_packages

with io.open('README.md', encoding='utf-8') as readme:
    long_description = readme.read()

name = 'build_capi'
description = 'build C/C++ static libraries (compile/link to build directory)'


setup_params = dict(
    name=name,
    version='0.0.1',
    author="Danilo Horta",
    author_email="danilo.horta@gmail.com",
    description=description,
    long_description=long_description,
    url="https://github.com/Horta/" + name,
    packages=find_packages(),
    zip_safe=False,
    use_scm_version=True,
    install_requires=[],
    extras_require={},
    setup_requires=['pytest-runner', 'setuptools_scm'],
    tests_require=['pytest'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Operating System :: OS Independent",
        "Framework :: Pytest",
    ],
    entry_points={
        'distutils.commands': [
            'build_capi = build_capi.build_capi:build_capi',
            'install_capi = build_capi.install_capi:install_capi',
        ],
    },
    include_package_data=True,
)

if __name__ == '__main__':
    setuptools.setup(**setup_params)
