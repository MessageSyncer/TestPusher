from model import *
from util import *
import image


class TestPusher(Pusher):
    async def push(self, content: Struct, to: str) -> PushResult:
        try:
            print(f'=> Pushing {content} to {to}')
            ok = True
            _e = None
        except Exception as e:
            ok = False
            _e = e
        return PushResult(ok, _e)
