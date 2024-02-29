import sys


if __name__ == "__main__":
    file = len(sys.argv) > 1
    if file:
        try:
            with open(sys.argv[1]) as f:
                s = [el.rstrip() for el in f.readlines()]
        except Exception as e:
            raise e

    cnt = 1
    while True:
        try:
            _s = s.pop(0) if file else input()
            print(f"{cnt}\t{_s}")
            cnt += 1
        except (IndexError, KeyboardInterrupt, EOFError):
            break
