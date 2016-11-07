# build_capi

Build and distribute C/C++ static libraries via Python packages

## Getting Started

You can have a ``setup.py`` similar to

```python
>>> from os.path import join
>>> from setuptools import setup
>>>
>>> def get_lib():
...     from build_capi import CApiLib
>>>
>>>      mylib = CApiLib('pkg_name.lib.nmylib',
...                      sources=[join('pkg_name', 'sources', 'example.c')],
...                      include_dirs=[join('pkg_name', 'include')]
...      )
...
>>> setup(
...     name='pkg_name',
...     # ...
...     setup_requires=['build_capi'],
...     capi_libs=[get_lib],
...     include_package_data=True,
...     data_files=[(join('pkg_name', 'include'), join('pkg_name', 'include',
                                                       'example.h'))],
...     package_data={'': [join('pkg_name', 'lib', '*.*')]},
... )
...
```

and then have a ``pkg_name/__init__.py``

```python
>>> def get_include():
...     import pkg_name
...     from os.path import join, dirname
...     return join(dirname(pkg_name.__file__), 'include')
...
>>> def get_lib():
...     import pkg_name
...     from os.path import join, dirname
...     return join(dirname(pkg_name.__file__), 'lib')
...
```

Please, refer to [build_capi/example/prj_name](build_capi/example/prj_name)
for a minimal example of project using ``build_capi``.

### Installing

Via pip
```
pip install build_capi
```

or via [Conda](http://conda.pydata.org/docs/index.html)
```
conda install -c conda-forge build_capi
```

## Running the tests

After installation, you can test it
```
python -c "import build_capi; build_capi.test()"
```

## Authors

* **Danilo Horta** - [https://github.com/Horta](https://github.com/Horta)

## License

This project is licensed under the MIT License - see the
[LICENSE](LICENSE) file for details
