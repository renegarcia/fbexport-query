# Fbexport Query

Exports queries from an Firebird database. This is a wrapper for [fbexport](https://fbexport.sourceforge.net/fbexport.php). See the section on configuration if it is not in your `PATH`.


### Usage


```
usage: fbexport-query.py [-h] [--out OUT] db sql

positional arguments:
  db          Database location.
  sql         File with SQL query to execute.

options:
  -h, --help  show this help message and exit
  --out OUT   Output location. Use '-' for stdout (default).
```


### Finding fbexport

`fbexport-query` first tries to read the location of `fbexport` from an environment variable named `FBEXPORT`. If unsuccessful, it tries to read it from a file named `CONFIG.ini`, whose structure is simply

```
[DEFAULT]
FBEXPORT = /path/to/fbexport
```

then it tries to find it in the system PATH, raising an `FbexportError` if none of the methods above succeeded.
