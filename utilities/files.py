

import os
import inspect


def path_relative_to_file(path: str) -> str:
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = module.__file__

    root = os.path.dirname(filename)

    return os.path.join(root, path)
