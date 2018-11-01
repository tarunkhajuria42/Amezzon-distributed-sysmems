import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;

public class IpAddressTest {

    public static void main(String[] args) throws Exception {
        String systemIp = "";
        try{
            URL  url_name = new URL("http://bot.whatismyipaddress.com");
            BufferedReader sc = new BufferedReader(new InputStreamReader(url_name.openStream()));
            systemIp = sc.readLine().trim();
        }catch (Exception e){
            systemIp = "Cannot execute";
        }
        System.out.println("Public IP address " + systemIp);
    }
}
