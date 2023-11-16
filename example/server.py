"""
Run client.py to consume this server's data.
The server gets the privacy policy of its map methods from config.yaml.
"""

from fedmed import Server
from waitress import serve

server = Server(config="config.yaml")
if __name__ == "__main__":
    server["test1"] = {"dim": [1]}
    server["test2"] = {"dim": [2, 3]}
    serve(server.app, host="127.0.0.1", port=8000)