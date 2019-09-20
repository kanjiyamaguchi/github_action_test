# coding: utf-8

class HelloPython:

    def __init__(self, message=None):
        self.message = message

    def hello(self):

        try:
            print(self.message)

        except Exception as e:
            print(e)
            return False

        return True


if __name__ == "__main__":

    string = "hello"
    hello_python = HelloPython(message=string)
    hello_python.hello()
