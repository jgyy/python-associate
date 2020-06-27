# python -m exception_handling.using_exceptions
import sys

from exception_handling.cli import main
from exception_handling.cli.errors import ArgumentError

try:
    main()
except ArgumentError as err:
    print(f"Error: {err}")
    sys.exit(1)
