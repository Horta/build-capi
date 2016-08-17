from os.path import join
import ncephes
from setuptools import setup
from build_capi import add_capi_opts
setup = add_capi_opts(setup)
from build_capi import CApiLib

mylib = CApiLib('pkg_name.lib.mylib',
                sources=[join('pkg_name', 'sources', 'example.c')],
                include_dirs=[join('pkg_name', 'sources'),
                              ncephes.get_include()],
                libraries=['m', 'ncprob'],
                library_dirs=[ncephes.get_lib()]
                )


setup_params = dict(
    name='pkg_name',
    author="Danilo Horta",
    author_email="danilo.horta@gmail.com",
    description='description',
    long_description='long description',
    setup_requires=['build_capi'],
    capi_libs=[mylib]
)

if __name__ == '__main__':
    setup(**setup_params)
