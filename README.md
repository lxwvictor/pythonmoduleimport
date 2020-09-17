There is a huge difference to load module when python file run as script (e.g. `python main.py`) or module (e.g. `python -m main`). It also impacts how `__init__.py` file is loaded and its objects are imported.

1. Loaded as script, e.g, `python testimport/main.py`, or `python main.py`, python visibiity limits WITHIN in the script\'s parent DIRECTORY, the visibility doesn't include the directory itself, absolute import is based on the directory visibility, unable to perform relative import
2. Loaded as top level "module", e.g, `python -m main`, visibility limits WITHIN current DIRECTORY, the visibility doesn't include the directory itself, absolute import is based on the directory visibility, unable to perform relative import
3. Loaded as part of a package, e.g, `python -m testimport.main`, visibility available to current PACKAGE, use absolute import by specifying package full path, or use `.` for relative import

Rule of thumb: The value of `__package__` determines the package or directory visibility. Run to the `.sh` files in `TestImport` and its subdirectory to understand the details.