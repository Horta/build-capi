from __future__ import unicode_literals

from subprocess import check_output
import sys
import os

def test_build():
    path_ = __import__('build_capi').__path__[0]
    src_path = os.path.abspath(path_)
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        ps = [p for p in sys.path if 'build_capi' in p]
        e = ''
        for p in ps:
            e += '%s:' % p
        e = 'PYTHONPATH=' + e + '$PYTHONPATH'
        cmd = 'cd ../example/prj_name/ && env %s python setup.py build' % e
        o = check_output(cmd, shell=True, universal_newlines=True)
        assert('running build' in o)
    finally:
        os.chdir(old_path)
