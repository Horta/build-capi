def get_include():
    import pkg_name
    from os.path import join, dirname
    d = join(dirname(pkg_name.__file__), 'include')
    return d


def get_lib():
    import pkg_name
    from os.path import join, dirname
    d = join(dirname(pkg_name.__file__), 'lib')
    return d
