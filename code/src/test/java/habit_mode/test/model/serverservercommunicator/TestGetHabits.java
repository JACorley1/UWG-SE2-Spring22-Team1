package habit_mode.test.model.serverservercommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Random;

import com.google.gson.Gson;
import com.google.gson.internal.LinkedTreeMap;
import com.google.gson.reflect.TypeToken;

import org.junit.jupiter.api.Test;
import org.zeromq.SocketType;
import org.zeromq.ZContext;
import org.zeromq.ZMQ;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;
import habit_mode.model.SuccessCode;

public class TestGetHabits {
    private class TrueMockServer extends Thread {
        private final Type TYPE = new TypeToken<HashMap<String, Object>>() { } .getType();
        private final String succ = "success_code";
        @Override
        public void run() {
            
            try (ZContext context = new ZContext()) {
                // Socket to talk to clients
                ZMQ.Socket socket = context.createSocket(SocketType.REP);
                socket.bind("tcp://*:5554");
                HashMap<String, Object> map1 = new HashMap<String, Object>();
                HashMap<String, Object> response = new HashMap<String, Object>();
                ArrayList<LinkedTreeMap<String, Object>> map = new ArrayList<LinkedTreeMap<String, Object>>();
                List<Habit> habits = new ArrayList<Habit>();
                Gson gson = new Gson();
                int responses = 0;
                while (responses < 100) {
                    // Block until a message is received
                    HashMap<String, Object> reply = gson.fromJson(socket.recvStr(), TYPE);

                    switch ((String) reply.get("request_type")) {
                        case "register_user":
                            map1 = reply;
                            response.put(succ, 00);
                            socket.send(gson.toJson(response));
                            response.clear();
                            break;
                        case "login":
                            if (map1.containsValue(reply.get("username")) && map1.containsValue(reply.get("password"))) {
                                response.put(succ, 00);
                                response.put("authentication_token", "1");
                                socket.send(gson.toJson(response));
                                response.clear();
                                break;
                            } else {
                                response.put(succ, 15);
                                socket.send(gson.toJson(response));
                                response.clear();
                                break;
                            }
                        case "add_habit":
                            LinkedTreeMap<String, Object> habit1 = new LinkedTreeMap<String, Object>();
                            habit1.put("frequency", 0.0);
                            habit1.put("id", 1);
                            habit1.put("name", reply.get("habit_name"));
                            habit1.put("is_complete", false);
                            map.add(habit1);
                            response.put(succ, 00);
                            socket.send(gson.toJson(response));
                            response.clear();
                            break;
                        case "complete_habits":
                            map.get(0).replace("is_complete", true);
                            response.put(succ, 00);
                            response.put("coins", 70);
                            socket.send(gson.toJson(response));
                            response.clear();
                            break;
                        case "retrieve_data":
                            response.put("habits", map);
                            response.put("coins", 70);
                            response.put(succ, 00);
                            socket.send(gson.toJson(response));
                            response.clear();
                            break;
                    }
    
                    responses++;
                }   
            } catch (Exception e) {
                this.interrupt();
            }
        }
    }
    @Test
    void testNoHabits(){
        ServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5554");
        TrueMockServer server = new TrueMockServer();
        server.start();
        Random rand = new Random();
        String username = rand.nextInt() + "";
        communicator.registerCredentials(username, "password", "email");

        communicator.validateLogin(username, "password");
        List<Habit> habits = communicator.getHabits();
        server.interrupt();
        assertEquals(0, habits.size());

    }
    @Test
    void testOneHabit(){
        ServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5554");
        TrueMockServer server = new TrueMockServer();
        server.start();
        Random rand = new Random();
        String username = rand.nextInt() + "";
        communicator.registerCredentials(username, "password", "email");

        communicator.validateLogin(username, "password");
        Habit habit = new Habit("text", Frequency.DAILY);
        communicator.addHabit(habit);

        List<Habit> habits = communicator.getHabits();
        server.interrupt();
        assertEquals(1, habits.size());
        assertEquals(habit, habits.get(0));

    }
    @Test
    void testMultipleHabits(){
        ServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5554");
        TrueMockServer server = new TrueMockServer();
        server.start();
        Random rand = new Random();
        String username = rand.nextInt() + "";
        communicator.registerCredentials(username, "password", "email");

        communicator.validateLogin(username, "password");
        Habit habit1 = new Habit("text", Frequency.DAILY);
        Habit habit2 = new Habit("test", Frequency.DAILY);
        communicator.addHabit(habit1);
        communicator.addHabit(habit2);

        List<Habit> habits = communicator.getHabits();
        server.interrupt();
        assertEquals(2, habits.size());
        assertEquals(habit1, habits.get(0));
        assertEquals(habit2, habits.get(1));
    }
}
