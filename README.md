There is a huge difference to load module when python file run as script (e.g. `python main.py`) or module (e.g. `python -m main`). It also impacts how `__init__.py` file is loaded and its objects are imported.

1. Loaded as script, e.g, `python testimport/main.py`, or `python main.py`. Alternatively, go to each level of directory and then run `./run_as_sript.sh` from all levels of directories. Python visibility limits WITHIN but exclude the script\'s parent DIRECTORY (`testimport`). Absolute import is based on the (within) directory visibility, unable to perform relative import. `__package__: None`
    - Succeeded, `import foo`   # visibility within the directory only
    - Failed, `import testimport.foo`   # visibility exclude the directory, `testimport` is unrecognized
    - Failed, `from testimport import foo`  # visibility exclude the directory, `testimport` is unrecognized
    - Failed, `from . import foo`   # unable to perform relative import
2. Loaded as top level "module", e.g, `python -m main`. Alternatively, `cd TestImport/testimport; ./run_as_module.sh`. Python visibility limits WITHIN but exclude current DIRECTORY (`testimport`). Absolute import is based on the (within) directory visibility, unable to perform relative import. `__package__:`
    - Succeeded, `import foo`   # visibility within the directory only
    - Failed, `import testimport.foo`   # visibility is WITHIN but exclude `testimport`, so `testimport` is unrecognized
    - Failed, `from testimport import foo`  # visibility is WITHIN but exclude `testimport`, so `testimport` is unrecognized
    - Failed, `from . import foo`   # unable to perform relative import
3. Loaded as part of a package, e.g, `python -m testimport.main`. Alternatively, `cd TestImport; ./run_as_module.sh`. Python visibility available to current PACKAGE (`testimport`). Absolute import by specifying package full path, e.g, `testimport.***`. Or use `.` for relative import. `__package__: testimport`
    - Failed, `import foo`  # visibility is package `testimport`, need to specify the full path, starting from `testimport`
    - Succeeded, `import testimport.foo`    # visibility is package `testimport`, and it does start from `testimport`
    - Succeeded, `from testimport import foo`   # visibility is package `testimport`, and it does start from `testimport`
    - Succeeded, `from . import foo`    # visibility is package `testimport`, use relative import
    - Failed, `from .. import upper_most_module`    # visibility is package `testimport` and it's already the top level, the `..` goes beyond that
4. Loaded as part of a package, e.g, `python -m Test.testimport.main`. Alternatively, `./run_as_module.sh`. Python visibility available to current PACKAGE (`TestImport.testimport`). Absolute import by specifying package full path, e.g, `TestImport.***`. Or use `.` for relative import. `__package__: TestImport.testimport`
    - Failed, `import foo`  # visibility is package `TestImport.testimport`, need to specify the full path, starting from `TestImport`
    - Failed, `import testimport.foo`    # visibility is package `TestImport.testimport`, need to specify the full path, starting from `TestImport`
    - Failed, `from testimport import foo`   # visibility is package `TestImport.testimport`, need to specify the full path, starting from `TestImport`
    - Succeeded, `import TestImport.testimport.foo` # visibility is package `TestImport.testimport`, and it does start from `TestImport`
    - Succeeded, `from . import foo`    # visibility is package `TestImport.testimport`, use relative import
    - Succeeded, `from .. import upper_most_module`    # visibility is package `TestImport.testimport`, so `..` is actually `TestImport`, it's still in scope

Rule of thumb: The value of `__package__` determines the package or directory visibility. Run the `.sh` files each level of directory to understand more details.

**DO NOTE**, python on Windows using Cygwin doesn't seem to work in that way, but who cares!?