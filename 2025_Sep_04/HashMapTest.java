import java.util.HashMap;
import java.util.Map;

class HashMapTest {
    public static void main(String[] args) {
       Map<String,String> userInfo = new HashMap<String,String>();

       userInfo.put("name", "John");
       userInfo.put("role", "Admin");
       userInfo.put("dept", "IT");
       userInfo.put("city", "Bengaluru");

       for (Map.Entry<String,String>entry: userInfo.entrySet()) {
            System.out.printf("%s -> %s\n", 
                              entry.getKey(), entry.getValue());
       }

    }

}
