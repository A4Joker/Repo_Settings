import java.util.*;

public class bad_named_class {
    
    // VIOLATION: Hardcoded credentials
    private static final String DB_PASSWORD = "mysecret123";
    public String name;
    public static final int maxsize = 100;
    
    public void Bad_Named_Method() {
        if (true)
            System.out.println("no braces");
            
        // VIOLATION: Magic number without constant
        for (int i = 0; i < 10; i++) {
            // VIOLATION: Inefficient string concatenation in loop
            String result = "";
            for (int j = 0; j < 5; j++) {
                result += "data" + j;
            }
        }
        
        // VIOLATION: Empty catch block
        try {
            int x = 10 / 0;
        } catch (Exception e) {
        }
        
        // VIOLATION: Deep nesting (4 levels)
        if (true) {
            if (true) {
                if (true) {
                    if (true) {
                        System.out.println("too deep");
                    }
                }
            }
        }
        
        // VIOLATION: Code duplication
        printUserInfo("John", 25);
        printUserInfo("Jane", 30);
        printUserInfo("Bob", 35);
    }
    
    // VIOLATION: Function too long and does multiple things
    public void doEverything() {
        // VIOLATION: No input validation
        String userInput = getUserInput();
        processData(userInput);
        
        // VIOLATION: Resource not closed properly
        FileInputStream file = new FileInputStream("data.txt");
        // ... use file but never close it
        
        // VIOLATION: SQL injection vulnerability
        String query = "SELECT * FROM users WHERE name = '" + userInput + "'";
        
        // Many more lines making function too long...
        for (int i = 0; i < 100; i++) {
            // VIOLATION: Repeated expensive operation
            String data = loadFromDatabase();
            process(data);
        }
    }
    
    // VIOLATION: Duplicated code pattern
    private void printUserInfo(String name, int age) {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("-------------------");
    }
    
    // VIOLATION: No error handling
    private String getUserInput() {
        Scanner scanner = new Scanner(System.in);
        return scanner.nextLine();
    }
    
    // VIOLATION: No input validation
    private void processData(String data) {
        // VIOLATION: Potential XSS if output to web
        System.out.println("Processing: " + data);
    }
    
    // VIOLATION: Expensive operation called repeatedly
    private String loadFromDatabase() {
        // Simulate expensive database call
        try { Thread.sleep(100); } catch (InterruptedException e) {}
        return "data";
    }
    
    private void process(String data) {
        // Empty method
    }
    
    public static List<String> cache = new ArrayList<>();
}
