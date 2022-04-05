from backend.server import Server
from backend.authentication_manager import AuthenticationManager
from backend.service_manager import ServiceManager

def main():
    """
    The main entry point for the application
    """
    server = Server()
    server.run(ServiceManager(), AuthenticationManager())

if __name__ == "__main__":
    main()