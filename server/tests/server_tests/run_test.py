import json
from socket import socket
from typing import Tuple
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

def run_server(server: Server, socket_info: Tuple[str, int] = ("127.0.0.1", 5555), context: zmq.Context = zmq.Context()):
    server.run(socket_info, ServiceManager(), AuthenticationManager(), context)

class ExceptionContext(zmq.Context):
    exception_socket = None

    def socket(self, socket_type, **kwargs):
        self.exception_socket = ExceptionSocket()
        return self.exception_socket

class ExceptionSocket(zmq.Socket):
    hits = 0
    responses = []

    def __init__(self, *a, **kw):
        pass

    def recv_string(self):
        if self.hits == 0:
            self.hits += 1
            return json.dumps({
                "request_type": "register_user", 
                "username": "test", 
                "password": "test", 
                "email": "email@email.com"
            })
        else:
            return json.dumps("exit")
    
    def bind(self, addr):
        pass

    def close(self, linger=None):
        pass
    
    def send_string(self, string, flags=0, copy=True, track=False):
        self.responses.append(string)

class ExceptionServiceManager(ServiceManager):
    def create_user(self, username: str, password: str, email: str) -> int:
        raise Exception()

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

    def test_context_is_none(self):
        """
        Tests that the server raises an error if the context is None
        """
        server = Server()
        with self.assertRaises(Exception):
            server.run(("localhost", 5555), ServiceManager(), AuthenticationManager(), None)
    
    def test_context_is_not_context(self):
        """
        Tests that the server raises an error if the context is not a context
        """
        server = Server()
        with self.assertRaises(Exception):
            server.run(("localhost", 5555), ServiceManager(), AuthenticationManager(), "not a context")

    def test_request_causes_exception(self):
        """
        Tests if the server handles exceptions correctly
        """
        server = Server()
        context = ExceptionContext()
        server.run(("localhost", 5555), ExceptionServiceManager(), AuthenticationManager(), context)
        
        response = context.exception_socket.responses[0]
        json_response = json.loads(response)
        success_code = json_response["success_code"]
        error_message = json_response["error_message"]

        self.assertEqual(success_code, 15, "Success code is 15")
        self.assertEqual(error_message, "Unknown error (Exception thrown)", "Check if error message is correct")