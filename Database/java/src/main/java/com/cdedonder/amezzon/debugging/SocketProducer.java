package com.cdedonder.amezzon.debugging;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class SocketProducer {

    private Socket socket;
    private ObjectMapper objectMapper;
    private PrintWriter pw;


    public SocketProducer() {
        try {
            socket = new Socket("localhost", 9111);
            objectMapper = new ObjectMapper();
            pw = new PrintWriter(socket.getOutputStream(), true);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void sendMessage(String action, String data) {
        try {
            System.out.println(action);
            pw.println(objectMapper.writeValueAsString(new DataTransferObject(LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_TIME), action, data)));
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void finalize() throws Throwable {
        pw.close();
        socket.close();
        super.finalize();
    }

    public class DataTransferObject {

        private String action, data;
        private String time;

        public DataTransferObject(String time, String action, String data) {
            this.time = time;
            this.action = action;
            this.data = data;
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

        public String getTime() {
            return time;
        }

        public void setTime(String time) {
            this.time = time;
        }
    }

}
