import sys


if __name__ == "__main__":
    files = len(sys.argv) > 1
    tot = len(sys.argv) > 2
    if files:
        s = [f for f in sys.argv[1:]]

    l, w, b = 0, 0, 0
    while True:
        try:
            if files:
                f = s.pop(0)
                _w, _b = 0, 0
                with open(f) as _f:
                    fl = _f.readlines()
                    for _l in fl:
                        _w += len(_l.split())
                        _b += len(_l.encode())

                    print(f"\t{len(fl)}\t{_w}\t{_b} {f}")
                    l += len(fl)
                    w += _w
                    b += _b
            else:
                _s = input()
                l += 1
                w += len(_s.split())
                b += len(_s.encode())
        except IndexError:
            if tot:
                print(f"\t{l}\t{w}\t{b} total")
            break
        except (KeyboardInterrupt, EOFError):
            print(f"\n\t{l}\t{w}\t{b}")
            break
        except FileNotFoundError as e:
            print(e)
