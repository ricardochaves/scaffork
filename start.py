#!/usr/bin/env python
import sys

from scaffork.controller import main


def patched_main() -> None:
    if len(sys.argv) == 1:
        main(".scaffork.yml")
    main(sys.argv[1])


if __name__ == "__main__":
    patched_main()
