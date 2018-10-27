package com.cdedonder.amezzon;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.URL;

public class HttpConnectionTest {

    public static void main(String[] args) throws Exception {
        String url = "http://127.0.0.1:8123";

        HttpURLConnection connection = (HttpURLConnection) new URL(url).openConnection();
        connection.setRequestMethod("GET");
        connection.setDoOutput(true);

        try (PrintWriter writer = new PrintWriter(connection.getOutputStream(), true)) {
            ObjectMapper mapper = new ObjectMapper();
            String message = mapper.writeValueAsString(new DebugMessage());
            writer.println(message);
        }

        System.out.println("Response code: " + connection.getResponseCode());

        try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println("Response: " + line);
            }
        }
    }

    @SuppressWarnings("WeakerAccess")
    private static class DebugMessage {
        private String action = "debug message";
        private String data;

        public DebugMessage(String message){
            data = message;
        }

        public DebugMessage(){
            this("Hello World!");
        }

        public String getAction() {
            return action;
        }

        public void setAction(String action) {
            this.action = action;
        }

        public String getData() {
            return data;
        }

        public void setData(String data) {
            this.data = data;
        }
    }
}
