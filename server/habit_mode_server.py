from server import Server
from authentication_manager import AuthenticationManager
from service_manager import ServiceManager

def main():
    """
    The main entrypoint for the application
    """
    server = Server()
    server.run(ServiceManager(), AuthenticationManager())

if __name__ == "__main__":
    main()