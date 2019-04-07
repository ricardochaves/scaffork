import sys

from scaffork.controller import main

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main(".scaffork.yml")
    main(sys.argv[1])
