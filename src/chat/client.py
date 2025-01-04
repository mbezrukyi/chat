import socket


class Client:
    FAMILY = socket.AF_INET
    TYPE = socket.SOCK_STREAM

    def __init__(self, host: str, port: int):
        self.socket = socket.socket(
            family=self.FAMILY,
            type=self.TYPE,
        )
        self.socket.connect((host, port))

    def send(self, data: bytes) -> None:
        self.socket.sendall(data)

    def receive(self) -> bytes:
        return self.socket.recv(1024)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.socket.close()


def run() -> None:
    with Client(host="127.0.0.1", port=8000) as client:
        client.send("some".encode())

        print(f"Received: {client.receive().decode()}")
