from os.path import join
from setuptools import setup


def get_lib():
    from build_capi import CApiLib

    mylib = CApiLib('pkg_name.lib.nmylib',
                    sources=[join('pkg_name', 'sources', 'example.c')],
                    include_dirs=[join('pkg_name', 'include')]
    )

    return mylib


setup_params = dict(
    name='pkg_name',
    author="Danilo Horta",
    author_email="danilo.horta@gmail.com",
    description='description',
    long_description='long description',
    setup_requires=['build_capi'],
    capi_libs=[get_lib],
    include_package_data=True,
    data_files=[(join('pkg_name', 'include'), join('pkg_name', 'include',
                                                   'example.h'))],
    package_data={'': [join('pkg_name', 'lib', '*.*')]},
)

if __name__ == '__main__':
    setup(**setup_params)
