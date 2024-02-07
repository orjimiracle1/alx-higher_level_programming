#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    le = len(sys.argv) - 1
    print("{} argument{}{}"
          .format(le, "" if le == 1 else "s", "." if le == 0 else ":"))
    for i in range(le):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
