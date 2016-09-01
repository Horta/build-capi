import io
from os.path import join

import setuptools
from setuptools import find_packages

with io.open('README.md', encoding='utf-8') as readme:
    long_description = readme.read()

setup_params = dict(
    name='build_capi',
    version='0.1.0',
    author="Danilo Horta",
    author_email="danilo.horta@gmail.com",
    description='build C/C++ static libraries (compile/link to build' +
                ' directory)',
    long_description=long_description,
    url="https://github.com/Horta/build_capi",
    packages=find_packages(),
    zip_safe=False,
    setup_requires=['pytest-runner'],
    install_requires=['pytest', 'six'],
    tests_require=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
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
        ],
        'distutils.setup_keywords': [
            'capi_libs = build_capi.setuptools_ext:capi_libs',
        ],
    },
    include_package_data=True,
)

try:
    from distutils.command.bdist_conda import CondaDistribution
except ImportError:
    pass
else:
    setup_params['distclass'] = CondaDistribution
    setup_params['conda_buildnum'] = 1
    setup_params['conda_features'] = ['mkl']

if __name__ == '__main__':
    setuptools.setup(**setup_params)
