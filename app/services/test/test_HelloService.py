import unittest

from app.services.HelloService import HelloService


class HelloServiceTest(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.hello_service = HelloService()

    def test_get_message(self):
        self.assertEqual(self.hello_service.get_message(), "Hello")
        self.assertNotEqual(self.hello_service.get_message(), "Bye")
