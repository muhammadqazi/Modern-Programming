from pathlib import Path

# prefix components:
space =  '    '
branch = '│   '
# pointers:
tee =    '├── '
last =   '└── '


def tree(dir_path: Path, prefix: str=''):
    """A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters
    """
    contents = list(dir_path.iterdir())
    ## ignore __pycache__ , __idea__, .git , env
    contents = [x for x in contents if not x.name.startswith('env')]
    contents = [x for x in contents if not x.name.startswith('.idea')]
    contents = [x for x in contents if not x.name.startswith('.git')]
    contents = [x for x in contents if not x.name.startswith('__pycache__')]
    contents = [x for x in contents if not x.name.startswith('venv')]
    contents = [x for x in contents if not x.name.startswith('vscode')]

    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir(): # extend the prefix and recurse:
            extension = branch if pointer == tee else space
            # i.e. space because last, └── , above so no more |
            yield from tree(path, prefix=prefix+extension)

for line in tree(Path.home() / 'path/to/directory'):
    print(line)
