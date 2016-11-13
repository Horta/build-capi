from __future__ import unicode_literals

from subprocess import check_output
import sys
import os

def test_example():
    src_path = os.path.dirname(os.path.realpath(__file__))
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        ps = [p for p in sys.path if 'build_capi' in p]
        e = ''
        for p in ps:
            e += '%s:' % p
        e = 'PYTHONPATH=' + e + '$PYTHONPATH'
        cmd = 'cd ../prj_name/ && env %s python setup.py build' % e
        o = check_output(cmd, shell=True, universal_newlines=True)
        assert('running build' in o)
    finally:
        os.chdir(old_path)
