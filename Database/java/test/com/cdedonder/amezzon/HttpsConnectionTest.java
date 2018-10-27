package com.cdedonder.amezzon;

import javax.net.ssl.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.URL;
import java.security.KeyStore;
import java.security.SecureRandom;

//http://javasourcecode.org/2016/12/04/implementing-https-client-in-java-part-1/

public class HttpsConnectionTest {

    public static void main(String[] args) {

        /*String https_url = "https://127.0.0.1:8123";
        URL url;
        System.setProperty("https.protocols", "TLSv1,TLSv1.1,TLSv1.2");
        try {
            url = new URL(https_url);
            HttpsURLConnection connection = (HttpsURLConnection) url.openConnection();

            SSLContext SSL_CONTEXT = SSLContext.getInstance("TLSv1.2");
            //KeyManager[] km = getKeyManager();
            TestClass test = new TestClass();
            SSL_CONTEXT.init(km, new TrustManager[]{test}, new SecureRandom());
            connection.setSSLSocketFactory(SSL_CONTEXT.getSocketFactory());
            connection.setHostnameVerifier(test);

            connection.setRequestMethod("POST");
            connection.setDoOutput(true);

            try (PrintWriter writer = new PrintWriter(connection.getOutputStream(), true)) {
                writer.println("Hello Server!");
            }

            System.out.println("Response code: " + connection.getResponseCode());

            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println("Response: " + line);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }*/
    }

    private static KeyManager[] getKeyManager(String filepath, String password, String keyPassword) {
        KeyStore ks = null;
        try {
            char[] storepass = password.toCharArray();
            char[] keypass = keyPassword.toCharArray();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public static class TestClass implements TrustManager, HostnameVerifier {
        @Override
        public boolean verify(String s, SSLSession sslSession) {
            return false;
        }

    }
}
