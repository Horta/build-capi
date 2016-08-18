from .setup import add_capi_opts
from .capi_lib import CApiLib
from .build_capi import build_capi

def test():
    import os
    p = __import__('build_capi').__path__[0]
    src_path = os.path.abspath(p)
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        return_code = __import__('pytest').main([])
    finally:
        os.chdir(old_path)

    return return_code
