import asyncio
async def main():
    print("===START===")
    import socket
    global socket

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind(('0.0.0.0', 2222))
    socket.listen(10)
    main_loop.create_task(while_func())

async def while_func():
    while True:
        connect, addr = socket.accept()
        while True:
            data = connect.recv(1024)
            if str(data) == 'close':
                connect.close()
                break

            connect.send(data)
            connect.close()

main_loop = asyncio.new_event_loop()
main_loop.run_until_complete(main())
main_loop.run_forever()