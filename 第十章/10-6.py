import contextlib
@contextlib.contextmanager
def my_mgr(s,e):
    print(s)
    yield s +' '+e
    print(e)
if __name__ == '__main__':
    with my_mgr('start','end') as val:
        print(val)
