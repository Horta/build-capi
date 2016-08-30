import os
import sys

from setuptools.command.build_ext import build_ext

# import distutils.core
# distutils.core._setup_stop_after = 'commandline'

from build_capi import CApiLib

try:
    basestring
except NameError:
    # Python 3.x
    basestring = str


def capi_libs(dist, attr, value):
    assert attr == 'capi_libs'
    if isinstance(value, basestring):
        value = [value]

    for capi_lib in value:
        _check_capi_lib(dist, capi_lib)

    cmdclass = dist.cmdclass
    _build_ext = _process_build_ext(cmdclass.pop('build_ext', build_ext))
    cmdclass['build_ext'] = _build_ext
    dist.cmdclass = cmdclass


def _check_capi_lib(dist, capi_lib):
    if not isinstance(capi_lib, CApiLib):
        error("argument to 'capi_libs=...' must be a CApiLib or a list" +
              " of CApiLib," +
              " not %r" % (type(capi_lib).__name__,))


def _process_build_ext(klass):
    def run(self):
        self.reinitialize_command('build_capi', inplace=self.inplace,
                                  build_clib=self.build_lib)
        self.run_command("build_capi")
        return klass.old_run(self)
    klass.old_run = klass.run
    klass.run = run
    return klass
