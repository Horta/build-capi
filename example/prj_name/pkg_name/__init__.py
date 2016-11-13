def get_include():
    import pkg_name
    from os.path import join, dirname
    return join(dirname(pkg_name.__file__), 'include')

def get_lib():
    import pkg_name
    from os.path import join, dirname
    return join(dirname(pkg_name.__file__), 'lib')
