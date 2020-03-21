print('__package__:', __package__)
if __package__ is None:
    # uses current directory visibility
    print('Loaded as top level script, uses current directory visibility only, absolute import is based on current directory visibility, unable to perform relative import\n')
elif __package__ == '':
    # uses current directory visibility
    print('Loaded as top level "module", uses current directory visibility only, absolute import is based on current directory visibility, unable to perform relative import\n')
else:
    # uses current package visibility
    print('Loaded as part of a package, uses current package visibility, use either absolute import by specifying package full path, or use "." for relative import\n')

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
    from . import foo
    print('Succeeded, "from . import foo"\n')
except:
    print('Failed, "from . import foo"\n')
    pass

try:
    from . import *
    print('Succeeded, "from . import *", import all the objects from __init__.py, it\'s different from loading/running __init__.py during module import')
    print_init()
except:
    print('Failed, "from . import *"\n')
    pass