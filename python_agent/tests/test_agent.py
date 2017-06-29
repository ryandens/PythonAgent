from unittest import TestCase
import python_agent


class TestAgent(TestCase):

    def test_agent(self):
        s = python_agent.test()
        self.assertEqual(s, "This is a test")