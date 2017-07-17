import asyncio
# 从Python 3.5开始 可以让coroutine的代码更简洁易读
# 把@asyncio.coroutine替换为async；
# 把yield from替换为await。

# @asyncio.coroutine
async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    # reader, writer = yield from connect
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    # yield from writer.drain()
    await writer.drain()
    while True:
        # line = yield from reader.readline()
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
