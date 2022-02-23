package habit_mode;

import java.io.IOException;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Parent;
import javafx.scene.Scene;

/**
 * Entry point for the program
 *
 * @author	Shawn Carter
 * @version Fall 2021
 */
public class Main extends Application {
    public static final String WINDOW_TITLE = "Habit Mode";
    public static final String GUI_RESOURCE = "view/codebehind/LoginScreen.fxml";

    /**
     * JavaFX entry point.
     *
     * @precondition none
     * @postcondition none
     *
     * @throws IOException
     */
    @Override
    public void start(Stage primaryStage) throws IOException {
        Parent parent = FXMLLoader.load(getClass().getResource(Main.GUI_RESOURCE));
        Scene scene = new Scene(parent);
        primaryStage.setTitle(WINDOW_TITLE);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    /**
     * Primary Java entry point.
     *
     * @precondition none
     * @postcondition none
     *
     * @param args command line arguments
     */
    public static void main(String[] args) {
        Main.launch(args);
    }
}
