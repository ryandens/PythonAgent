
class AgentString(object):
    COUNT = 0

    def __init__(self, value):
        print("hello init")
        AgentString.COUNT += 1
        self.value = value

    def __add__(self, other):
        print("hello add")
        AgentString.COUNT += 1
        return self.value + other.value

    def __call__(self, *args, **kwargs):
        print("hello call")
        return self.value
