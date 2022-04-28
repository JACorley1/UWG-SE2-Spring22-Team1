# Habit Mode

Habit Mode is a habit-reinforcement application that encourages the development of good habits through positive feedback. Habit Mode manages a list of habits that the user adds, allowing them to be easily checked off as they are completed. Habits will be automatically reset after a specified period of time, allowing the user to focus squarely on completing their tasks instead of managing the list itself.

## Testing
- Client tests can be run through Maven
  - Coverage can be checked by opening `code/target/site/jacoco/index.html`
- Server tests are run using the `/server/tests/run_tests.bat` script.
  - The `coverage` and `pytest` modules must be installed through pip to run the script.
  - Coverage can be checked by opening `server/tests/htmlcov/index.html`.
  - Adding `-o` will display the code coverage in a webpage immediately after finishing.

## Running
1. Ensure python's zmq module is installed by running `pip install zmq`.
2. Run `/server/habit_mode_server.py`. The server will launch at `127.0.0.1:5555` by default.
   - `-h <host>` can be used to specify the IP address.
   - `-p <port>` can be used to specify the port.
3. Move to the `code/` directory.
4. Launch the client by with `mvn javafx:run`.
5. On the title screen, register for an account.
6. Once the account has been successfully registered, you will be logged in automatically.
