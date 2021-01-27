import os, sys
print('I am from testimport/main.py')
print('__package__:', __package__)
print('CWD is %s' % os.getcwd())
# print('sys.path is %s' % sys.path)

if __package__ is None:
    # uses current directory visibility, exclude the directory itself, hence no relative import
    print('Loaded as script, e.g, `python testimport/main.py`, or `python main.py`.')
    print('Visibility: WITHIN but exclude the script\'s parent DIRECTORY (`testimport`).')
    print('Absolute import: WITHIN the script\'s parent directory, as limited by the visibility.')
    print('Relative import: Unable to perform relative import, e.g, `.`.')
    print('`__package__: None`\n')
elif __package__ == '':
    # uses current directory visibility, exclude the directory itself, hence no relative import
    print('Loaded as top level "module", e.g, `python -m main`.')
    print('Visibility: WITHIN but exclude the script\'s parent DIRECTORY (`testimport`).')
    print('Absolute import: WITHIN the script\'s parent directory, as limited by the visibility.')
    print('Relative import: Unable to perform relative import, e.g, `.`.')
    print('`__package__:`\n')
elif __package__ == 'testimport':
    # uses current package visibility
    print('Loaded as part of a package, e.g, `python -m testimport.main`.')
    print('Visibility: Current PACKAGE (`testimport`).')
    print('Absolute import: Import by specifying package full path, e.g, `testimport.***`')
    print('Relative import: Doable as long as the path doesn\'t go beyond the top level package, e.g, `.`, `..`')
    print('`__package__: testimport`\n')
elif __package__ == 'TestImport.testimport':
    # uses current package visibility
    print('Loaded as part of a package, e.g, `python -m TestImport.testimport.main`.')
    print('Visibility: Current PACKAGE (`TestImport.testimport`).')
    print('Absolute import: Import by specifying package full path, e.g, `TestImport.***`')
    print('Relative import: Doable as long as the path doesn\'t go beyond the top level package, e.g, `.`, `..`')
    print('`__package__: TestImport.testimport`\n')
else:
    print('Some other import ways, have fun!')

try:
    import foo
    print('Succeeded, "import foo"\n')
except:
    print('Failed, "import foo"\n')

try:
    from . import foo
    print('Succeeded, "from . import foo"\n')
except:
    print('Failed, "from . import foo"\n')

try:
    import TestImport.testimport.foo
    print('Succeeded, "import TestImport.testimport.foo"\n')
except:
    print('Failed, "import TestImport.testimport.foo"\n')

try:
    from TestImport.testimport import foo
    print('Succeeded, "from TestImport.testimport import foo"\n')
except:
    print('Failed, "from TestImport.testimport import foo"\n')

try:
    import testimport.foo
    print('Succeeded, "import testimport.foo"\n')
except:
    print('Failed, "import testimport.foo"\n')

try:
    from testimport import foo
    print('Succeeded, "from testimport import foo"\n')
except:
    print('Failed, "from testimport import foo"\n')

try:
    import subpackage1.module1
    print('Succeeded, "import subpackage1.module1"\n')
except:
    print('Failed, "import subpackage1.module1"\n')

try:
    import testimport.subpackage1.module1
    print('Succeeded, "import testimport.subpackage1.module1"\n')
except:
    print('Failed, "import testimport.subpackage1.module1"\n')

try:
    from . import *
    print('Succeeded, "from . import *", import all the objects from __init__.py but not executing the file. It\'s different from loading __init__.py during importing or running as module, e.g, `import testimport`, or, `python -m testimport.main`. In such cases, the file is also executed.')
    print_init()
except:
    print('Failed, "from . import *"\n')

try:
    from .. import upper_most_module
    print('Succeeded, "from .. import upper_most_module" is also possible as long as the relative path is within the scope of top level of the "__package__"')
    upper_most_module.hello()
    print()
except:
    print('Failed, "from .. import upper_most_module"\n')

try:
    from ... import *
    print('Succeeded, "from ... import *" is also possible as long as the relative path is within the scope of top level of the "__package__"')
except:
    print('Failed, "from ... import *"\n')