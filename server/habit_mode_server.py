from server import Server
from service_manager import ServiceManager

def main():
    """
    The main entrypoint for the application
    """
    server = Server()
    server.run(ServiceManager())

if __name__ == "__main__":
    main()