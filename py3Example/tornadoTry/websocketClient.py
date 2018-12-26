# -*- coding: utf-8 -*-
# Created by bida on 2018/8/16
import time
import websocket

try:
    import thread
except ImportError:
    import _thread as thread

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print('### server closed ###')

def on_open(ws):
    def run(*args):
        for i in range(10):
            time.sleep(1)
            ws.send(f'hello {i}')
        time.sleep(1)
        ws.close()
        print('thread terminating')

    thread.start_new_thread(run, ())

if __name__ == '__main__':
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp('ws://localhost:5002',
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()