package com.cdedonder.amezzon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.URL;

public class HttpConnectionTest {

    public static void main(String[] args) throws Exception {
        String url = "http://127.0.0.1:8123";

        HttpURLConnection connection = (HttpURLConnection) new URL(url).openConnection();
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
    }
}
