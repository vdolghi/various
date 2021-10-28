class Hello:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        print (f"Hello, {self.func(*args)}!")

@Hello
def name():
    return "world"

if __name__ == '__main__':
    name()