import socket


class Server:
    FAMILY = socket.AF_INET
    TYPE = socket.SOCK_STREAM

    def __init__(self, host: str, port: int):
        self.socket = socket.socket(
            family=self.FAMILY,
            type=self.TYPE,
        )
        self.socket.bind((host, port))

    def start(self) -> None:
        self.socket.listen(3)
        client, addr = self.socket.accept()

        self._process(client, addr)

    def _process(self, client: socket.socket, addr: tuple[str, int]) -> None:
        with client:
            print(f"Connected by: {addr}")

            while True:
                data = client.recv(1024)

                if not data:
                    break

                client.sendall(data)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.socket.close()


def run() -> None:
    with Server(host="127.0.0.1", port=8000) as server:
        server.start()
