import json
import unittest
import zmq
import threading
import time
from backend.server import Server
from backend.authentication_manager import AuthenticationManager
from backend.service_manager import ServiceManager

def create_client_socket():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:5555")
    return socket

def run_server(server: Server):
    server.run(("127.0.0.1", 5555), ServiceManager(), AuthenticationManager())

class TestRun(unittest.TestCase):    
    """
    Tests for the run method.

    @author Team 1
    @version Spring 2022
    """

    def test_run_and_register_user(self):
        """
        Runs the server, registers a user, and closes the server.
        """
        server = Server()
        thread = threading.Thread(target=run_server, args=(server,))
        thread.start()

        socket = create_client_socket()

        socket.send_string(json.dumps({
            "request_type": "register_user",
            "username": "test",
            "password": "test",
            "email": "email@email.com",
        }))
        json_response = socket.recv_string()
        json.loads(json_response)

        socket.send_string(json.dumps("exit"))
        
        thread.join()
    
    def test_socket_info_is_not_tuple(self):
        """
        Tests that the server raises an error if the socket info is not a tuple.
        """
        server = Server()
        with self.assertRaises(Exception):
            server.run("not a tuple", ServiceManager(), AuthenticationManager())

    def test_socket_info_not_enough_items(self):
        """
        Tests that the server raises an error if the socket info has less than two items
        """
        server = Server()
        with self.assertRaises(Exception):
            server.run(("localhost",), ServiceManager(), AuthenticationManager())
    
    def test_socket_info_too_many_items(self):
        """
        Tests that the server raises an error if the socket info has more than two items
        """
        server = Server()
        with self.assertRaises(Exception):
            server.run(("localhost", "5555", "extra"), ServiceManager(), AuthenticationManager())
    
    def test_socket_info_first_item_not_string(self):
        """
        Tests that the server raises an error if the socket info first item is not a string
        """
        server = Server()
        with self.assertRaises(Exception):
            server.run((5555,), ServiceManager(), AuthenticationManager())
    
    def test_socket_info_second_item_not_int(self):
        """
        Tests that the server raises an error if the socket info second item is not an int
        """
        server = Server()
        with self.assertRaises(Exception):
            server.run(("localhost", "not an int"), ServiceManager(), AuthenticationManager())
    
    def test_service_manager_not_service_manager(self):
        """
        Tests that the server raises an error if the service manager is not a ServiceManager
        """
        server = Server()
        with self.assertRaises(Exception):
            server.run(("localhost", 5555), "not a ServiceManager", AuthenticationManager())
    
    def test_authentication_manager_not_authentication_manager(self):
        """
        Tests that the server raises an error if the authentication manager is not an AuthenticationManager
        """
        server = Server()
        with self.assertRaises(Exception):
            server.run(("localhost", 5555), ServiceManager(), "not an AuthenticationManager")
