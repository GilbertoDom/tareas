#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""

    Script para ejecutar el Servidor

"""

import asyncio
# import main
import server_utils

if __name__ == "__main__":
    address = ("192.168.100.32", 8080)
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(server_utils.handle_conversation, *address, reuse_port=True)
    server = loop.run_until_complete(coro)
    print("Listening at {}".format(address))

    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()
# EOF
