package com.cdedonder.amezzon.debugging;

import com.cdedonder.amezzon.logging.DatabaseLogger;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.logging.Logger;

public class SocketProducer {

    private static final Logger LOGGER = DatabaseLogger.getLogger();

    private Socket socket;
    private ObjectMapper objectMapper;
    private PrintWriter pw;


    public SocketProducer() {
        try {
            socket = new Socket("localhost", 9111);
            pw = new PrintWriter(socket.getOutputStream(), true);
            objectMapper = new ObjectMapper();
        } catch (IOException e) {
            LOGGER.info("Database intercept not active.");
        }
    }

    public void sendMessage(String action, String data) {
        if (pw == null) return;
        try {
            pw.println(objectMapper.writeValueAsString(new DataTransferObject(LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_TIME), action, data)));
        } catch (JsonProcessingException e) {
            LOGGER.severe(e.getMessage());
        }
    }

    @Override
    protected void finalize() throws Throwable {
        if (pw != null) pw.close();
        if (socket != null) socket.close();
        super.finalize();
    }

    @SuppressWarnings("unused")
    public class DataTransferObject {

        private String action, data, time;

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
