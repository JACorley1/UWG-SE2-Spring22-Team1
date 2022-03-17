package habit_mode.model.local_implementation;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.Scanner;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import org.zeromq.SocketType;
import org.zeromq.ZMQ;
import org.zeromq.ZContext;

public class ServerServerCommunicator {
    public static void main(String[] args) throws Exception {
        HashMap<String, String> message;
        Gson gson;
        String REQUEST_TYPE = "request_type";
        Scanner scanner;
        String username;
        String password;
        String email;
        String jsonMessage;

        try (ZContext context = new ZContext()) {
            System.out.println("Connecting to tcp://127.0.0.1:5555...");

            ZMQ.Socket socket = context.createSocket(SocketType.REQ);
            socket.connect("tcp://127.0.0.1:5555");

            scanner = new Scanner(System.in);

            message = new HashMap<String, String>();
            message.put(REQUEST_TYPE, "register_user");

            System.out.println("Username?");
            username = scanner.nextLine();
            message.put("username", username);
            System.out.println("Password?");
            password = scanner.nextLine();
            message.put("password", password);
            System.out.println("Email?");
            email = scanner.nextLine();
            message.put("email", email);

            gson = new Gson();

            jsonMessage = gson.toJson(message);

            socket.send(jsonMessage);

            Type type = new TypeToken<HashMap<String, Object>>(){}.getType();

            String jsonResponse = socket.recvStr();
            HashMap<String, Object> response = gson.fromJson(jsonResponse, type);

            System.out.println("Received reply: " + response);

            message.clear();

            message.put(REQUEST_TYPE, "login");

            System.out.println("Username?");
            username = scanner.nextLine();
            System.out.println("Password");
            password = scanner.nextLine();
            message.put("username", username);
            message.put("password", password);

            jsonMessage = gson.toJson(message);

            socket.send(jsonMessage);

            jsonResponse = socket.recvStr();
            response = gson.fromJson(jsonResponse, type);

            System.out.println("Received reply: " + response);

            String token = (String) response.get("authentication_token");
        }
    }
}