from model import *
import image


class TestPusher(Pusher):
    async def push(self, content: Struct, to: str) -> PushResult:
        try:
            # print(f'This article will be pushed to {to}: ')
            # print('==================')
            # print(content.asmarkdown())
            # print('==================')
            self.logger.info('Pushing...')
            ok = True
            _e = None
        except Exception as e:
            ok = False
            _e = e
        return PushResult(ok, _e)
