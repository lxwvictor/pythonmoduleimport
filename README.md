There is a huge difference to load module when python file run as script or module. It also impacts how `__init__.py` file is loaded and its objects are imported.

1. Loaded as top level script, uses current directory visibility only, absolute import is based on current directory visibility, unable to perform relative import
2. Loaded as top level "module", uses current directory visibilityonly, absolute import is based on current directory visibility, unable to perform relative import
3. Loaded as part of a package, uses current package visibility, use either absolute import by specifying package full path, or use `.`` for relative import

Rule of thumb: The value of `__package__` determines the package or directory visibility. Run to the `.sh` files in `TestImport` and its subdirectory to understand the details.