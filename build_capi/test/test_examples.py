import os
from subprocess import check_output

def test_build():
    p = __import__('build_capi').__path__[0]
    src_path = os.path.abspath(p)
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        cmd = 'cd build_capi/examples/prj_name && python setup.py build'
        o = check_output(cmd, shell=True)
        assert(o == 'running build\n')
    finally:
        os.chdir(old_path)
