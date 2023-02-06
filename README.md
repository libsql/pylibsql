pylibsql
========

This library is a fork of [pysqlite3] that links to [libSQL][libsql]. It
provides the same interface as the `sqlite3` package in the Python standard
library.

[pysqlite3]: https://github.com/coleifer/pysqlite3
[libsql]: https://libsql.org/

Build and install libSQL
------------------------

This package depends on [libSQL][libsql] being installed on your system. You can
build and install libSQL from source as follows:

```
$ git clone https://github.com/libsql/libsql
$ cd libsql
$ make liblibsql.la
$ sudo make liblibsql_install
```
