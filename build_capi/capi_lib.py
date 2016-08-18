from six import string_types
from types import ListType


class CApiLib(object):

    def __init__(self, name, sources,
                 include_dirs=None,
                 define_macros=None,
                 undef_macros=None,
                 library_dirs=None,
                 libraries=None,
                 runtime_library_dirs=None,
                 extra_objects=None,
                 extra_compile_args=None,
                 extra_link_args=None,
                 export_symbols=None,
                 depends=None):

        assert isinstance(name, string_types), "'name' must be a string"
        assert (type(sources) is ListType and
                all([isinstance(s, string_types) for s in sources])), \
            "'sources' must be a list of strings"

        self.name = name
        self.sources = sources
        self.include_dirs = include_dirs or []
        self.define_macros = define_macros or []
        self.undef_macros = undef_macros or []
        self.library_dirs = library_dirs or []
        self.libraries = libraries or []
        self.runtime_library_dirs = runtime_library_dirs or []
        self.extra_objects = extra_objects or []
        self.extra_compile_args = extra_compile_args or []
        self.extra_link_args = extra_link_args or []
        self.export_symbols = export_symbols or []
        self.depends = depends or []
