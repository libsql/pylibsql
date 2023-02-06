# -*- coding: ISO-8859-1 -*-
# setup.py: the distutils script
#
import os
import setuptools
import sys

from distutils import log
from distutils.command.build_ext import build_ext
from setuptools import Extension

# If you need to change anything, it should be enough to change setup.cfg.

PACKAGE_NAME = 'pylibsql'
VERSION = '0.1.0'

# define sqlite sources
sources = [os.path.join('src', source)
           for source in ["module.c", "connection.c", "cursor.c", "cache.c",
                          "microprotocols.c", "prepare_protocol.c",
                          "statement.c", "util.c", "row.c", "blob.c"]]

# define packages
packages = [PACKAGE_NAME]
EXTENSION_MODULE_NAME = "._libsql"

# Work around clang raising hard error for unused arguments
if sys.platform == "darwin":
    os.environ['CFLAGS'] = "-Qunused-arguments"
    log.info("CFLAGS: " + os.environ['CFLAGS'])


def quote_argument(arg):
    q = '\\"' if sys.platform == 'win32' and sys.version_info < (3, 9) else '"'
    return q + arg + q

define_macros = [('MODULE_NAME', quote_argument(PACKAGE_NAME + '.dbapi2'))]


class SystemLibSqliteBuilder(build_ext):
    description = "Builds a C extension linking against libsql library"

    def build_extension(self, ext):
        log.info(self.description)

        # For some reason, when setup.py develop is run, it ignores the
        # configuration in setup.cfg, so we just explicitly add liblibsql.
        # Oddly, running setup.py build_ext -i (for in-place) works fine and
        # correctly reads the setup.cfg.
        ext.libraries.append('libsql')
        build_ext.build_extension(self, ext)


def get_setup_args():
    return dict(
        name=PACKAGE_NAME,
        version=VERSION,
        description="DB-API 2.0 interface for libSQL",
        long_description='',
        author="ChiselStrike, Charles Leifer",
        author_email="info@chiselstrike.com",
        license="zlib/libpng",
        platforms="ALL",
        url="https://github.com/libsql/pylibsql",
        package_dir={PACKAGE_NAME: "pylibsql"},
        packages=packages,
        ext_modules=[Extension(
            name=PACKAGE_NAME + EXTENSION_MODULE_NAME,
            sources=sources,
            define_macros=define_macros)
        ],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: zlib/libpng License",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX",
            "Programming Language :: C",
            "Programming Language :: Python",
            "Topic :: Database :: Database Engines/Servers",
            "Topic :: Software Development :: Libraries :: Python Modules"],
        cmdclass={
            "build_ext": SystemLibSqliteBuilder
        }
    )


if __name__ == "__main__":
    setuptools.setup(**get_setup_args())
