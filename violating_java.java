import java.util.*;

// Violates: Class name should be PascalCase
public class bad_named_class {
    
    // Violates: Should be private with getter
    public String name;
    
    // Violates: Should be UPPER_SNAKE_CASE
    public static final int maxsize = 100;
    
    // Violates: Method name should be camelCase
    public void Bad_Named_Method() {
        // Violates: No braces for if statement
        if (true)
            System.out.println("no braces");
            
        // Violates: Magic number
        for (int i = 0; i < 10; i++) {
            // Violates: String concatenation in loop
            String result = "";
            for (int j = 0; j < 5; j++) {
                result += "data" + j;
            }
        }
        
        // Violates: Empty catch block
        try {
            int x = 10 / 0;
        } catch (Exception e) {
        }
        
        // Violates: Deep nesting
        if (true) {
            if (true) {
                if (true) {
                    if (true) {
                        System.out.println("too deep");
                    }
                }
            }
        }
    }
    
    // Violates: Method too long and does multiple things
    public void doEverything() {
        // 60+ lines of mixed functionality
        // ... imagine many lines here doing different things ...
        String data = "start";
        for (int i = 0; i < 100; i++) {
            data += " more data " + i;
            if (i % 10 == 0) {
                System.out.println(data);
                data = "reset";
            }
            try {
                process(data);
            } catch (Exception e) {
                // Violates: Generic exception catch
            }
        }
        // ... many more lines ...
    }
    
    private void process(String data) {
        // Empty method
    }
    
    // Violates: Public static field that's not a constant
    public static List<String> cache = new ArrayList<>();
}
