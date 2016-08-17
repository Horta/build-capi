import os
from subprocess import check_output

def test_build():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    src_path = os.path.abspath(dir_path)
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        cmd = 'cd ../examples/prj_name && python setup.py build'
        o = check_output(cmd, shell=True)
        assert(o == 'running build\n')
    finally:
        os.chdir(old_path)
