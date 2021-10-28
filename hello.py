class Hello:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print (f"Hello, {self.name}!")
    def set(self, name):
        self.name = name
    def get(self):
        return self.name

if __name__ == '__main__':
    name = input("What is your name? ")
    greeter = Hello(name)
    greeter.greet()

