"""Main file for pyTodo."""
from commands import commands as cmds
import sys
if __name__ == '__main__':
    print("This is the main file of the pyTodo package.")
    try:
        cmds.pytd()
    except cmds.ValidationException as e:
        print(e)
        print("Exiting...")
        sys.exit(1)
    except Exception as e:
        print(e)
        print("Exiting...")
        sys.exit(1)