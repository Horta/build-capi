from subprocess import check_output

def test_build():
    cmd = 'python examples/prj_name/setup.py build'
    o = check_output(cmd, shell=True)
    assert(o == 'running build\n')
