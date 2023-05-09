
from distutils.core import setup, Extension

import sys

options = {'py2exe': {}}
scripts = ['PyritePublisher/pyrpub']

if sys.platform == 'win32':
    import py2exe

    from PyritePublisher import pp_meta
    import string
    py2exe_opts = {'includes': string.join(['PyritePublisher.'+x for x in pp_meta.plugin_modules],',') }
    options['py2exe'] = py2exe_opts
    scripts.append('PyritePublisher/pyrpub_gui.pyw')
    

setup(name = "pyrite-publisher",
      version = "2.1.1",
      description = "Content creation tools for Palm users",
      author = "Rob Tillotson",
      author_email = "rob@pyrite.org",
      url = "http://www.pyrite.org/",

      ext_modules = [Extension("PyritePublisher._Doc",["PyritePublisher/_Doc.c"])],
      packages = ['PyritePublisher'],
      scripts = scripts,
      options = options,
      )
