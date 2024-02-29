import sys


BUF_LIMIT = 17
FILE_LIMIT = 10


if __name__ == "__main__":
    files = len(sys.argv) > 1
    if files:
        s = [f for f in sys.argv[1:]]

    buf = []
    while True:
        try:
            if files:
                f = s.pop(0)
                print(f"==> {f} <==")
                with open(f) as _f:
                    r = [el.rstrip() for el in _f.readlines()]
                    [print(el) for el in r[-FILE_LIMIT:]]
            else:
                buf.append(input())
                if len(buf) > BUF_LIMIT:
                    buf.pop(0)
        except IndexError:
            break
        except (KeyboardInterrupt, EOFError):
            print()
            [print(el) for el in buf]
            break
        except FileNotFoundError as e:
            print(e)
