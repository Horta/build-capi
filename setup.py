import io
from os.path import join

import setuptools
from setuptools import find_packages

with io.open('README.md', encoding='utf-8') as readme:
    long_description = readme.read()

setup_params = dict(
    name='build_capi',
    version='0.0.2',
    author="Danilo Horta",
    author_email="danilo.horta@gmail.com",
    description='build C/C++ static libraries (compile/link to build' +
                ' directory)',
    long_description=long_description,
    url="https://github.com/Horta/build_capi",
    packages=find_packages(),
    zip_safe=False,
    install_requires=['pytest'],
    extras_require={},
    setup_requires=['pytest', 'pytest-runner'],
    install_requires=['pytest'],
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

try:
    from distutils.command.bdist_conda import CondaDistribution
except ImportError:
    setup_params['distclass'] = CondaDistribution
    setup_params['conda_buildnum'] = 1
    setup_params['conda_features'] = ['mkl']

if __name__ == '__main__':
    setuptools.setup(**setup_params)
