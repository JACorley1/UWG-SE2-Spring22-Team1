from sys import argv
from backend.server import Server
from backend.authentication_manager import AuthenticationManager
from backend.service_manager import ServiceManager

def get_socket_info():
    i: int = 1
    host: str = "127.0.0.1"
    port: int = 5555

    while i < len(argv):
        if argv[i] == "-p":
            port = int(argv[i + 1])
            print("Port: " + str(port))
            i += 2
        elif argv[i] == "-h":
            host = argv[i + 1]
            print("Host: " + str(host))
            i += 2
        else:
            print("Invalid argument: " + argv[i])
            exit()
    
    return host, port

def main():
    """
    The main entry point for the application
    """
    host, port = get_socket_info()

    server = Server()
    server.run((host, port), ServiceManager(), AuthenticationManager())

if __name__ == "__main__":
    main()