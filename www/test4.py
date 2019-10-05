import orm
import asyncio
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome', charset='utf8')
    u = User(name='Test3', email='test3@example.com',
             passwd='12367890', image='about:blank')
    await u.save()


if __name__ == '__main__':
    # print('a')
    loop = asyncio.get_event_loop()
    # print('b')
    loop.run_until_complete(test(loop))
    # print('c')
    loop.run_forever()
    # print('d')不执行，因为前面是死循环
