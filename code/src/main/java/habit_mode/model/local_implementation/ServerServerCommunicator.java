package habit_mode.model.local_implementation;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import org.zeromq.SocketType;
import org.zeromq.ZMQ;

import habit_mode.model.Habit;
import habit_mode.model.ServerCommunicator;
import habit_mode.model.SuccessCode;
import habit_mode.model.sudoku.SudokuPuzzle;

import org.zeromq.ZContext;

public class ServerServerCommunicator extends ServerCommunicator {
    private static final String REQUEST_TYPE = "request_type";
    private static final String REQUEST_TYPE_REGISTER_USER = "register_user";
    private static final String REQUEST_TYPE_LOGIN = "login";
    private static final String TCP_CONNECTION_ADDRESS = "tcp://0.0.0.0:8000";
    
    private static final ZContext context = new ZContext();

    private ZMQ.Socket socket;
    private Gson gson;
    private HashMap<String, String> message;
    private String jsonMessage;

    public ServerServerCommunicator(){
        this.socket = context.createSocket(SocketType.REQ);
        this.gson = new Gson();
        this.message = new HashMap<String, String>();
        this.message.put(REQUEST_TYPE, "");
    }

    public HashMap<String, String> getMessage() {
        return this.message;
    }

    public Gson getGson() {
        return this.gson;
    }

    public String getJsonMessage() {
        return this.jsonMessage;
    }

    public ZMQ.Socket getSocket() {
        return this.socket;
    }

    public ZContext getContext() {
        return context;
    }

    @Override
    public SuccessCode registerCredentials(String username, String password, String email) {
        return SuccessCode.OKAY;
    }

    

    

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
            System.out.println("Connecting to tcp://0.0.0.0:8000");

            ZMQ.Socket socket = context.createSocket(SocketType.REQ);
            socket.connect("tcp://0.0.0.0:8000");

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
            scanner.close();
        }
    }

    @Override
    public SuccessCode validateLogin(String username, String password) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public int getCoins() {
        // TODO Auto-generated method stub
        return 0;
    }

    @Override
    public List<Habit> getHabits() {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public SudokuPuzzle getSudokuPuzzle() {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public boolean setCoins(int amount) {
        // TODO Auto-generated method stub
        return false;
    }

    @Override
    public SuccessCode addHabit(Habit habit) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public SuccessCode removeHabit(Habit habit) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public SuccessCode completeHabit(Habit habit) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public SuccessCode updateSudokuPuzzle(SudokuPuzzle puzzle) {
        // TODO Auto-generated method stub
        return null;
    }
}