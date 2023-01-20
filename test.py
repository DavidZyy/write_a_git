#!/usr/bin/env python3

import os

if __name__ == "__main__":
    # print(os.path.join("c", "foo"))
    path = "asdf"
    print(*path[:-1])
    print(path[:-1])
    print(path)
