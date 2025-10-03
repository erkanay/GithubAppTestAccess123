import java.util.concurrent.ThreadLocalRandom;



public class ThreadLocalRandomExample {
    public static void main(String[] args) {
        // Get the current thread's ThreadLocalRandom
        ThreadLocalRandom random = ThreadLocalRandom.current();
        
        // Generate a random integer
        int randomInt = random.nextInt();
        System.out.println("Random Integer: " + randomInt);
        
        // Generate a random integer within a range (inclusive, exclusive)
        int rangeInt = random.nextInt(10, 21);  // 10 to 20
        System.out.println("Random Integer (10-20): " + rangeInt);
        
        // Generate a random double
        double randomDouble = random.nextDouble();
        System.out.println("Random Double: " + randomDouble);
        
        // Generate a random double within a range
        double rangeDouble = random.nextDouble(1.0, 10.0);
        System.out.println("Random Double (1.0-10.0): " + rangeDouble);
        
        // Generate a random boolean
        boolean randomBoolean = random.nextBoolean();
        System.out.println("Random Boolean: " + randomBoolean);
    }
}
import java.security.SecureRandom;

public class SecureRandomExample {
    public static void main(String[] args) {
        // Create a SecureRandom instance
        SecureRandom secureRandom = new SecureRandom();
        
        // Generate a random integer
        int randomInt = secureRandom.nextInt();
        System.out.println("Secure Random Integer: " + randomInt);
        
        // Generate a random integer with bounds
        int boundedInt = secureRandom.nextInt(100);
        System.out.println("Secure Random Integer (0-99): " + boundedInt);
        
        // Generate random bytes
        byte[] randomBytes = new byte[8];
        secureRandom.nextBytes(randomBytes);
        System.out.print("Random Bytes: ");
        for (byte b : randomBytes) {
            System.out.print(b + " ");
        }
        System.out.println();
        
        // Generate a secure token (as a hexadecimal string)
        byte[] tokenBytes = new byte[16];
        secureRandom.nextBytes(tokenBytes);
        StringBuilder token = new StringBuilder();
        for (byte b : tokenBytes) {
            token.append(String.format("%02x", b));
        }
        System.out.println("Secure Token: " + token);
    }
}
