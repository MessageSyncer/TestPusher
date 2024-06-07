from model import *
import image


class MockAPI():
    def push(self, string):
        return True


class TestPusher(Pusher):
    def __init__(self, id=None) -> None:
        super().__init__(id)
        self.api = MockAPI()

    async def push(self, content: Struct, to: str):
        if not self.api.push(str(content)):
            raise Exception('Failed to push to mockAPI')
