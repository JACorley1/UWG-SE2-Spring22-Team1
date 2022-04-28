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

import habit_mode.model.SuccessCode;
import habit_mode.model.sudoku.SudokuPuzzle;
import habit_mode.model.Habit;
import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;

public class TestBuyHint {
    private class TrueMockServer extends Thread {
        private final Type TYPE = new TypeToken<HashMap<String, Object>>() { } .getType();
        private final String succ = "success_code";
        @Override
        public void run() {
            
            try (ZContext context = new ZContext()) {
                // Socket to talk to clients
                ZMQ.Socket socket = context.createSocket(SocketType.REP);
                socket.bind("tcp://*:5557");
                HashMap<String, Object> map1 = new HashMap<String, Object>();
                HashMap<String, Object> response = new HashMap<String, Object>();
                ArrayList<LinkedTreeMap<String, Object>> map = new ArrayList<LinkedTreeMap<String, Object>>();
                LinkedTreeMap<String, Object> puzzle = new LinkedTreeMap<String, Object>();
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
                            response.put("sudoku_puzzle", puzzle);
                            response.put("habits", map);
                            response.put("coins", 70);
                            response.put(succ, 00);
                            socket.send(gson.toJson(response));
                            response.clear();
                            break;
                        case "generate_sudoku_puzzle" :
                            int[][] board = { 
                                { 0, 9, 2, 0, 0, 0, 0, 8, 6 },
                                { 0, 0, 3, 0, 2, 7, 0, 5, 9 },
                                { 0, 5, 1, 3, 0, 6, 0, 2, 4 },
                                { 2, 6, 0, 9, 7, 3, 8, 4, 1 },
                                { 4, 0, 9, 5, 0, 1, 2, 0, 3 },
                                { 3, 1, 7, 4, 0, 2, 9, 6, 5 },
                                { 0, 3, 6, 7, 0, 8, 5, 0, 2 },
                                { 0, 7, 0, 2, 0, 0, 6, 0, 0 },
                                { 0, 2, 0, 6, 0, 0, 4, 0, 0 } 
                            };
                            boolean[][] numberLocks = { 
                                { false, true, true, false, false, false, false, true, true },
                                { false, false, true, false, true, true, false, true, true },
                                { false, true, true, true, false, true, false, true, true },
                                { true, true, false, true, true, true, true, true, true },
                                { true, false, true, true, false, true, true, false, true },
                                { true, true, true, true, false, true, true, true, true },
                                { false, true, true, true, false, true, true, false, true },
                                { false, true, false, true, false, false, true, false, false },
                                { false, true, false, true, false, false, true, false, false } 
                            };
                            
                            puzzle.put("numbers", board);
                            puzzle.put("number_locks", numberLocks);
                            response.put("sudoku_puzzle", puzzle);
                            response.put(succ, 00);
                            socket.send(gson.toJson(response));
                            response.clear();
                            break;
                        case "update_sudoku_puzzle" :
                            
                            ArrayList<ArrayList<Double>> numberLists = (ArrayList<ArrayList<Double>>) reply.get("numbers");
                          
                            int[][] numbers = new int[numberLists.size()][numberLists.size()];
                
                            for (int row = 0; row < numberLists.size(); row++) {
                                for (int col = 0; col < numberLists.get(row).size(); col++) {
                                    numbers[row][col] = numberLists.get(row).get(col).intValue();
                                }
                            }
                
                            puzzle.replace("numbers", numbers);
                            response.put(succ, 00);
                            socket.send(gson.toJson(response));
                            break;
                        case "remove_habit":
                            map.clear();
                            response.put(succ, 00);
                            socket.send(gson.toJson(response));
                            response.clear();
                            break;
                        case "buy_hint":
                            response.put("number", 0);
                            response.put("row", 0);
                            response.put("col", 0);
                            response.put("coins", 0);
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
    void testBuyingHint() {
        TrueMockServer server = new TrueMockServer();
        ServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5557");
        server.start();

        int[] hint = communicator.buyHint();

        assertEquals(4, hint.length);


    }
    
}
