from subprocess import check_output
import sys

def test_build():
    ps = [p for p in sys.path if 'build_capi' in p]
    e = ''
    for p in ps:
        e += '%s:' % p
    e = 'PYTHONPATH=' + e + '$PYTHONPATH'
    cmd = 'env %s cd examples/prj_name/ && python setup.py build' % e
    o = check_output(cmd, shell=True)
    assert(o == 'running build\n')
