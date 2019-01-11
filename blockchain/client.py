#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""

    Script para ejecutar el Cliente

"""

import asyncio
import server_utils


async def handle_conversation(hostname, port, loop):
    reader, writer = await asyncio.open_connection(hostname, port, loop=loop)

    data = await server_utils.get_block(reader)
    print(data)
    more = await server_utils.get_block(reader)
    print(more)
    subscription = "Gilberto Dominguez"
    await server_utils.put_block(writer, subscription)

if __name__ == "__main__":
    hostname = "192.168.100.32"
    port = 8080
    loop = asyncio.get_event_loop()
    loop.run_until_complete(handle_conversation(hostname, port, loop))
    loop.close()
