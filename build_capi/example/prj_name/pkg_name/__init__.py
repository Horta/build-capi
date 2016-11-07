


def get_include():
    """
    Return the directory that contains the nCephes \\*.h header files.
    Extension modules that need to compile against nCephes should use this
    function to locate the appropriate include directory.
    Notes
    -----
    When using ``distutils``, for example in ``setup.py``.
    ::
        import ncephes as nc
        ...
        Extension('extension_name', ...
                include_dirs=[nc.get_include()])
        ...
    """
    import pkg_name
    from os.path import join, dirname
    d = join(dirname(pkg_name.__file__), 'include')
    return d


def get_lib():
    import pkg_name
    from os.path import join, dirname
    d = join(dirname(pkg_name.__file__), 'lib')
    return d
