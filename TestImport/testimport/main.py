import os, sys
print('I am from testimport/main.py')
print('__package__:', __package__)
print('CWD is %s' % os.getcwd())
# print('sys.path is %s' % sys.path)
if __package__ is None:
    # uses current directory visibility, exclude the directory itself, hence no relative import
    print('Loaded as script, e.g, `python testimport/main.py`, or `python main.py`, python visibility limits WITHIN but exclude the script\'s parent DIRECTORY (`testimport`). Absolute import is based on the (within) directory visibility, unable to perform relative import. `__package__: None`\n')
elif __package__ == '':
    # uses current directory visibility, exclude the directory itself, hence no relative import
    print('Loaded as top level "module", e.g, `python -m main`, visibility limits WITHIN but exclude current DIRECTORY (`testimport`). Absolute import is based on the (within) directory visibility, unable to perform relative import. `__package__:`\n')
else:
    # uses current package visibility
    print('Loaded as part of a package, e.g, `python -m testimport.main`, visibility available to current PACKAGE (`testimport`), use absolute import by specifying package full path, or use `.` for relative import. `__package__: testimport`\n')

try:
    import foo
    print('Succeeded, "import foo"\n')
except:
    print('Failed, "import foo"\n')
    pass

try:
    import testimport.foo
    print('Succeeded, "import testimport.foo"\n')
except:
    print('Failed, "import testimport.foo"\n')
    pass

try:
    from testimport import foo
    print('Succeeded, "from testimport import foo"\n')
except:
    print('Failed, "from testimport import foo"\n')
    pass

try:
    from . import foo
    print('Succeeded, "from . import foo"\n')
except:
    print('Failed, "from . import foo"\n')
    pass

try:
    import subpackage1.module1
    print('Succeeded, "import subpackage1.module1"\n')
except:
    print('Failed, "import subpackage1.module1"\n')
    pass

try:
    import testimport.subpackage1.module1
    print('Succeeded, "import testimport.subpackage1.module1"\n')
except:
    print('Failed, "import testimport.subpackage1.module1"\n')
    pass

try:
    from . import *
    print('Succeeded, "from . import *", import all the objects from __init__.py, it\'s different from loading/running __init__.py during module import')
    print_init()
except:
    print('Failed, "from . import *"\n')
    pass