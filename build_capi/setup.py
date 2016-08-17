import os
import sys
from setuptools.command.build_ext import build_ext


def add_capi_opts(setup_func):
    import distutils.core

    def wrapper(*args, **kwargs):
        from setuptools import setup
        capi_libs = kwargs.pop('capi_libs', [])
        distutils.core._setup_stop_after = 'commandline'

        cmdclass = kwargs.pop('cmdclass', {})
        _build_ext = _process_build_ext(cmdclass.pop('build_ext', build_ext))
        cmdclass['build_ext'] = _build_ext
        kwargs['cmdclass'] = cmdclass

        dist = setup_func(*args, **kwargs)
        dist.capi_libs = capi_libs
        return _finalize_setup(dist)
    return wrapper

def _process_build_ext(klass):
    def run(self):
        self.reinitialize_command('build_capi', inplace=self.inplace,
                                  build_clib=self.build_lib)
        self.run_command("build_capi")
        return klass.old_run(self)
    klass.old_run = klass.run
    klass.run = run
    return klass

def _finalize_setup(dist):
    from distutils.debug import DEBUG
    from distutils.errors import DistutilsError
    from distutils.errors import CCompilerError

    try:
        dist.run_commands()
    except KeyboardInterrupt:
        raise SystemExit("interrupted")
    except (IOError, os.error) as exc:
        if DEBUG:
            sys.stderr.write("error: %s\n" % (exc,))
            raise
        else:
            raise SystemExit("error: %s" % (exc,))

    except (DistutilsError,
            CCompilerError) as msg:
        if DEBUG:
            raise
        else:
            raise SystemExit("error: " + str(msg))

    return dist
