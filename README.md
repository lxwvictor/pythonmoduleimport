There is a huge difference to load module when python file run as script (e.g. `python main.py`) or module (e.g. `python -m main`). It also impacts how `__init__.py` file is loaded and its objects are imported.

1. Loaded as script, e.g, `python testimport/main.py`, or `python main.py`, python visibility limits WITHIN but exclude the script\'s parent DIRECTORY (`testimport`). Absolute import is based on the (within) directory visibility, unable to perform relative import. `__package__: None`
    - Succeeded, `import foo`   # visibility within the directory only
    - Failed, `mport testimport.foo`   # visibility exclude the directory
    - Failed, `from testimport import foo`  # visibility exclude the directory
    - Failed, `from . import foo`   # unable to perform relative import
2. Loaded as top level "module", e.g, `python -m main`, visibility limits WITHIN but exclude current DIRECTORY (`testimport`). Absolute import is based on the (within) directory visibility, unable to perform relative import. `__package__:`
    - Succeeded, `import foo`   # visibility within the directory only
    - Failed, `import testimport.foo`   # visibility exclude the directory
    - Failed, `from testimport import foo`  # visibility exclude the directory
    - Failed, `from . import foo`   # unable to perform relative import
3. Loaded as part of a package, e.g, `python -m testimport.main`, visibility available to current PACKAGE (`testimport`), use absolute import by specifying package full path, or use `.` for relative import. `__package__: testimport`
    - Failed, `import foo`  # visibility to current package, need to specify the top package testimport
    - Succeeded, `import testimport.foo`    # visibility to current package
    - Succeeded, `from testimport import foo`   # visibility to current package
    - Succeeded, `from . import foo`    # visibility to current package, use relative import

Rule of thumb: The value of `__package__` determines the package or directory visibility. Run to the `.sh` files in `TestImport` and its subdirectory to understand the details.