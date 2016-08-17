import os
import sys


def add_capi_opts(setup_func):
    import distutils.core

    def wrapper(*args, **kwargs):
        from setuptools import setup
        capi_libs = kwargs.pop('capi_libs', [])
        distutils.core._setup_stop_after = 'commandline'
        dist = setup_func(*args, **kwargs)
        dist.capi_libs = capi_libs
        return _finalize_setup(dist)
    return wrapper


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
