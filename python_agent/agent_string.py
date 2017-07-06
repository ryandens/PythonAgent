
class AgentString(object):
    COUNT = 0

    def __init__(self, value):
        AgentString.COUNT += 1
        self.value = value

    def __add__(self, other):
        AgentString.COUNT += 1
        return self.value + other.value
